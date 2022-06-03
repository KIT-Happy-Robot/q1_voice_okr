#!/usr/bin/env python
# -*- coding: utf-8 -*-
from happymimi_msgs.srv import StrTrg

#from happymimi_voice_msgs.srv import TTS
#音声認識
from happymimi_voice_msgs.srv import SpeechToText

import pickle
import rospy
import Levenshtein as lev
import os.path
from happymimi_voice_msgs.srv import GgiLearning
from happymimi_voice_msgs.srv import GgiLearningResponse
from nltk.tag.stanford import StanfordPOSTagger


object_name_00 = ["brown drink",'finish　training']

plase_name_00 = "on the tall and brown table"

file_path=os.path.expanduser('~/catkin_ws/src/happymimi_voice/config') #作成場所の指定
#nltkのモデルを読み込む
pos_tag = StanfordPOSTagger(model_filename = file_path + "/dataset/stanford-postagger/models/english-bidirectional-distsim.tagger",
                            path_to_jar = file_path + "/dataset/stanford-postagger/stanford-postagger.jar")


class GgiinStruction:
    def __init__(self):
        #nltkのモデルを読み込む
        #保存ファイルの初期化
        with open(file_path+'/object_file.pkl',"wb") as f:
            dictionary={'object_name':[],'object_feature':[],
                        'place_name':[],'place_feature':[]}
            pickle.dump(dictionary, f)
        #google speech to textが認識しやすいよう設定する単語をリスト化
        with open(file_path+'/ggi_params/place_name','r') as f:
            self.object_template=[line.strip() for line in f.readlines()]
        with open(file_path+'/ggi_params/place_name','r') as c:
            self.place_template=[line.strip() for line in c.readlines()]
        #pickleファイルに保存するデータを保存するリスト
        self.name=[]
        self.feature=[]
        print("Waiting for stt and tts")
        rospy.wait_for_service('/tts')
        rospy.wait_for_service('/stt_server')
        print("server is ready")
        self.stt=rospy.ServiceProxy('/stt_server',SpeechToText)
        self.server=rospy.Service('/ggi_learning_02',GgiLearning,self.register_object)
        self.tts=rospy.ServiceProxy('/tts', StrTrg)

    #オブジェクト認識と登録
    def register_object(self,req):
        end=False
        self.tts("please say the object.")
        #ものの登録
        for string in object_name_00:
            if not end:
                #short_str:短い単語を認識しやすくする　context_phrases:認識しやすくしたい単語のリスト　boost_value:登録した単語の認識度合いを調節
                #string=self.stt(short_str=True,
                #    context_phrases=self.object_template.append('finish　training'),
                #    boost_value=13.0)

                #finish trainingと認識したときpickleファイルに保存してリストを初期化
                if  lev.distance(string, 'finish　training')/(max(len(string), len('finish　training')) *1.00)<0.3:
                    self.WordGeneralization()
                    self.save_name('' , True)
                    self.name=[]
                    self.feature=[]
                    break

                self.tts(string + ' is this OK?')

            recognition = "yes"#self.stt(short_str=True,context_phrases=['yes','no','again'],
                    #boost_value=15.0)
            #認識した内容で良いかを確認
            #yesのときリストにその単語を追加
            if 'yes' in recognition:
                self.save_name(string , True,add=False)
                end=False
                self.tts('next')
            #noのときリストに追加しない
            elif 'no' in recognition:
                self.tts('please one more time')
                end=False
            #認識した内容を聞き取れなかったときもう一度発話
            elif 'again' in recognition:
                self.tts(string +' is this OK?')
                end=True

        self.tts('Please tell me the place.')
        #場所の登録
        while 1:
            if not end:
                #string=self.stt(short_str=True,
                #    context_phrases=self.place_template,
                #    boost_value=13.0)
                string = plase_name_00
                self.tts(string +' Is this OK?')

            recognition = "yes"#self.stt(short_str=True,context_phrases=['yes','no','again'],
                    #boost_value=15.0)

            if 'yes' in recognition:
                res=self.save_name(string , False)
                break

            elif 'no' in recognition:
                self.tts('please one more time')
                end=False

            elif 'again' in recognition:
                self.tts(string +' Is this OK?')
                end=True

        self.feature=[]
        self.name=[]


        return GgiLearningResponse(location_name=res)


    #単語の汎化を追加
    def WordGeneralization(self):
        with open(file_path+"/class_generalization.pkl","rb") as f:
            #辞書型でvalueは集合
            class_data1=pickle.load(f)

        with open(file_path+"/class_by_word2vec.pkl","rb") as w:
            #辞書型でvalueは集合
            class_data2=pickle.load(w)

        for str in self.name:
            for k,v in class_data1.items():
                if str in v:
                    self.name.append(k)

            for k,v in class_data2.items():
                if str in v and k not in self.name:
                    self.name.append(k)





    #保存  st=string ob=name or place(名前はTrue,場所はFalse) addはpickleファイルに保存するか否か
    def save_name(self,st,ob,add=True):
        #形態素解析を行う
        pos=pos_tag.tag(st.split())  #品詞分解

        for i in range(len(pos)):
            #形容詞であれば特徴に追加
            if pos[i][1]=='JJ':
                self.feature.append(pos[i][0])
            #名詞であれば名前に追加
            elif 'NN' in pos[i][1]:
                self.name.append(pos[i][0])
        if add:
            with open(file_path+'/object_file.pkl','rb') as web:
                dict_data=pickle.load(web)
            #オブジェクトの登録
            if ob:
                dict_data['object_name'].append(self.name)
                dict_data['object_feature'].append(self.feature)

                with open(file_path+'/object_file.pkl','wb') as f:
                    pickle.dump(dict_data, f)
            #場所の登録
            else:
                dict_data['place_name'].append(self.name)
                dict_data['place_feature'].append(self.feature)
                with open(file_path+'/object_file.pkl','wb') as f:
                    pickle.dump(dict_data, f)
                #場所に特徴が有るか無いか（有るときはfeatureとnameを紐付け）
                if dict_data['place_feature'][len(dict_data['place_feature'])-1]:
                    str=' '.join(dict_data['place_feature'][len(dict_data['place_feature'])-1])+' '+' '.join(dict_data['place_name'][len(dict_data['place_name'])-1])
                else:
                    str=' '.join(dict_data['place_name'][len(dict_data['place_name'])-1])
                print(dict_data)
                return str


if __name__=='__main__':
    rospy.init_node('ggi_learning_02')
    GgiinStruction()
    rospy.spin()
