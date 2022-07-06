#2022/06/03
from os import path
file_path = path.expanduser('~/catkin_ws/src/happymimi_voice/actplan_generator/resource/')

# f = "contact name at the back door introduce her to everyone in the room "
max_data = 50000

dict_word={}
dict_num={}
dict_num[0]="<PAD>"
dict_word["<PAD>"]=0
dict_word["<start>"]=1
dict_word["<end>"]=2
dict_num[2]="<end>"
dict_num[1]="<start>"
word_number=2

with open(file_path+'input_str.txt','r') as f:

    for i,str_line in enumerate(f):
        if (i>=max_data):
            break
        id_str=[dict_word["<start>"]]
        for word in str_line.replace("?"," ?").replace("."," .").replace("!"," !").split():
            if word in dict_word:
                id_str.append(dict_word[word])
            else:
                word_number=word_number+1
                dict_word[word]=word_number
                dict_num[word_number]=word
                id_str.append(dict_word[word])

            id_str.append(dict_word["<end>"])

        print(id_str)
# print(id_str)
