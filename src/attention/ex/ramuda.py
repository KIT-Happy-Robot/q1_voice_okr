# -*- coding: utf-8 -*-
import os
import pickle as pk
with open("../../../../happymimi_voice/actplan_generator/data/dict_word.pkl", "rb") as f:
    targ_lang = pk.load(f)
    targ_num = pk.load(f)

# BATCH_SIZE = int(20)
change_word = lambda x:[targ_num[int(i)] for i in x.split()]
# print(targ_num)
# x = "1 13 12"
def change_w(x):
    for i in x.split():
        a.append(targ_num[int(i)])

    print(a)
    return a
a  = list(map(change_word, [1,3,4,5,6,7,8,9,10,11,12,13,11,14,2]))
# print(x)
# print(change_w)
#print(a)
print(a)
