
import pickle as pk
import sys
import os
from pymagnitude import Magnitude
model_name="glove.840B.300d.magnitude"
print("model is %s" % model_name)
if input("Do you want to run?(y/n):") in 'y':
    pass
else:
    print("stop")
    sys.exit()

class_list=["food","drink","bottle"]
file_path=os.path.expanduser('~/catkin_ws/src/happymimi_voice/config/')
max_word=100 #汎化する用語の最大数
minimum_evaluation_value=0.5 #最小評価値
model=Magnitude(file_path + "/stanford/glove.840B.300d.magnitude")
add_word=[]
dict_class={}

for c in class_list:
    for word,value in model.most_similar([c],topn=max_word):
        #print(word, value)
        if value >= minimum_evaluation_value:
            add_word.append(word)
    dict_class[c]=set(add_word)
    add_word=[]
print(dict_class)
with open(file_path+"class_by_mg.pkl","wb") as f:
    pk.dump(dict_class,f)


