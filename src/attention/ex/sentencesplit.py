# -*- coding: utf-8 -*-
sentence = "please escort name to the location and you will find him at the location , and tell a joke"
str = "Please escort {name} to the {location}, you will find him at the {location}"
str_out = "escort{name}{location}Nonefindhim{location}None"
sentence_c = "could you tell me how many people in the room are"
sentence_ls=[]
str_ls = sentence_c.split()
# print(str_ls)

# delimiter_ls=[i for i,x in enumerate(str_ls) if "," in x or "and" in x]
delimiter_ls = []
for i,x in enumerate(str_ls):
    if "," in x or "and" in x:
        delimiter_ls.append(i) 

# print(delimiter_ls)
if len(delimiter_ls) == 1:
    sentence_ls.append(str_ls[:delimiter_ls[0]])
    sentene_ls.append(str_ls[delimiter_ls[0]+1:])

elif len(delimiter_ls) == 0:
    print(1)
    print(str_ls)

else:
    sentence_ls.append(str_ls[:delimiter_ls[0]])
    sentence_ls.append(str_ls[delimiter_ls[0]+1:delimiter_ls[1]])
    sentence_ls.append(str_ls[delimiter_ls[1]+2:])

print(sentence_ls)
# print(delimiter_ls)
sub_ls=[]
for i,word in enumerate(str_ls):
    sub_ls.append(word)
    if i%4==3:
        sentence_ls.append(sub_ls)
        sub_ls=[]

# print(sub_ls)
