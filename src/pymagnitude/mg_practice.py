#!/usr/bin/env python
# -*- coding: utf-8 -*-



from pymagnitude import Magnitude

file_path=('/home/kawara/catkin_ws/src/happymimi_voice/config/stanford/glove.840B.300d.magnitude')
mv = Magnitude(file_path)
print("data loading")
match = mv.most_similar("apple", topn=10)
print(match)


