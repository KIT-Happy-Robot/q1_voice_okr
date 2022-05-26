# -*- coding: utf-8 -*-
sentence = "please escort name to the location and you will find him at the location"
str = "Please escort {name} to the {location}, you will find him at the {location}"
str_out = "escort{name}{location}Nonefindhim{location}None"
sentence_ls=[]
str_ls = sentence.split()
# print(str_ls)

# delimiter_ls=[i for i,x in enumerate(str_ls) if "," in x or "and" in x]
delimiter_ls = 0
for i,x in enumerate(str_ls):
    if "," in x or "and" in x:
        delimiter_ls = i 

for i,num in enumerate(str_ls):
    if "and" in str_ls[i]:
        sentence_ls.append(str_ls[:i])
        sentence_ls.append(str_ls[i+1:])

    elif "," in str_ls[i]:
        sentence_ls.append(str_ls[:i])
        sentence_ls.append(str_ls[i:])

    else:
        continue
    # if i == 0:
        # if "and" in str_ls[i]:
            # sentence_ls.append(str_ls[:i])
        
        # else:
            # str_ls[i]=str_ls[i].replace(",","")
            # sentence_ls.append(str_ls[:i+1])
            
    # else:
        # str_ls[i]=str_ls[i].replace(",","")
        # if delimiter_ls-1 != i:
            # sentence_ls.append(str_ls[i+1:])
            
        # else:
            # sentence_ls.append(str_ls[i+1:])

print(sentence_ls)
# print(delimiter_ls)
sub_ls=[]
for i,word in enumerate(str_ls):
    sub_ls.append(word)
    if i%4==3:
        sentence_ls.append(sub_ls)
        sub_ls=[]

# print(sub_ls)
