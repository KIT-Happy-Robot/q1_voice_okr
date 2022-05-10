# -*- coding: utf-8 -*-
sentence = "pleaseescort{name}tothe{location},youwillfindhimatthe{location}"
str = "Please escort {name} to the {location}, you will find him at the {location}"
str_out = "escort{name}{location}Nonefindhim{location}None"
sentence_ls=[]
str_ls = str_out.split()
print(str_ls)

delimiter_ls=[i for i,x in enumerate(str_ls) if "," in x or "and" in x]
for i,num in enumerate(delimiter_ls):
    if i==0:
        if "and" in str_ls[num]:
            sentence_ls.append(str_ls[:num])
        else:
            str_ls[num]=str_ls[num].replace(",","")
            sentence_ls.append(str_ls[:num+1])
    else:
        str_ls[num]=str_ls[num].replace(",","")
        if len(delimiter_ls)-1 != i:
            sentence_ls.append(str_ls[num+1:delimiter_ls[i+1]])
        else:
            sentence_ls.append(str_ls[num+1:])

print(sentence_ls)

sub_ls=[]
for i,word in enumerate(str_ls):
    sub_ls.append(word)
    if i%4==3:
        sentence_ls.append(sub_ls)
        sub_ls=[]

print(sub_ls)
