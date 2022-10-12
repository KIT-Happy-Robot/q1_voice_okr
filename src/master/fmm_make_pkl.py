#usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

file_path=os.path.expanduser('~/catkin_ws/src/q1_voice_okr/config')
with open(file_path + '/fmm_feature.pkl', "wb") as f:
    features = ["clothing","age","height","gender","skin color","hair color"]
    pickle.dump(features, f)

