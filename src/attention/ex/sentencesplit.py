# -*- coding: utf-8 -*-
<<<<<<< HEAD
sentence = "please escort name to the location and you will find him at the location , and tell a joke"
str = "Please escort {name} to the {location}, you will find him at the {location}"
=======
sentence = "pleaseescort{name}tothe{location},youwillfindhimatthe{location},tellhimjoke"
str_in = "Please escort {name} to the {location}, you will find him at the {location}"
>>>>>>> 32ce9eaa2becc0d9fa70377d496743a5f5f25f91
str_out = "escort{name}{location}Nonefindhim{location}None"
sentence_c = "could you tell me how many people in the room are"
sentence_ls=[]
<<<<<<< HEAD
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
sub=[]
for i,word in enumerate(str_ls):
    sub.append(word)
=======
str_ls = sentence.split()
str_ls_out = str_out.split()
del_ls = 0
delimiter_ls = []
# print(str_ls)

# delimiter_ls=[i for i,x in enumerate(str_ls) if "," in x or "and" in x]
# print(str_ls)
for i,x in enumerate(str_ls):
    if "," or "and" in x:
        del_ls += 1 

# print(del_ls)
delimiter_ls.append(del_ls)

for i,num in enumerate(delimiter_ls):
    if i==0:
        if "and" in str_ls[i]:
            sentence_ls.append(str_ls[:i])
        else:
            str_ls[i]=str_ls[i].replace(",","")
            sentence_ls.append(str_ls[:i+1])
    else:
        str_ls[i]=str_ls[i].replace(",","")
        if len(delimiter_ls)-1 != i:
            sentence_ls.append(str_ls[i+1:delimiter_ls[i+1]])
        else:
            sentence_ls.append(str_ls[i+1:])

print(delimiter_ls)
print(sentence_ls)


sub_ls=[]
for i,word in enumerate(str_ls_out):
    sub_ls.append(word)
>>>>>>> 32ce9eaa2becc0d9fa70377d496743a5f5f25f91
    if i%4==3:
        sentence_ls.append(sub)
        sub=[]

<<<<<<< HEAD
print(sub)
=======
# print(sub_ls)
>>>>>>> 32ce9eaa2becc0d9fa70377d496743a5f5f25f91
