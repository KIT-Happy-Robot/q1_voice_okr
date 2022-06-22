# magnitudeを準備。
from pymagnitude import Magnitude
import tensorflow as tf
from tensorflow import keras
import numpy as np

embedding= Magnitude("../../../../happymimi_voice/config/dataset/wiki-news-300d-1M-subword.magnitude") # ← さっき変換したデータ

# 似てる言葉を1000個探し、resultsに取得した配列を突っ込む。
# results = vectors.most_similar(u'location', topn = 10)

# resultsを表示。
#for result in results:
#    print(result)

def get_embedding(embedding,x):
    main_tf=[]
    for sentence in x:
        sub_tf=[]
        for word in sentence:
            sub_tf.append(embedding(word))
        main_tf.append(sub_tf)
    return tf.constant(main_tf)

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
a = get_embedding(embedding,x)
print(a)
