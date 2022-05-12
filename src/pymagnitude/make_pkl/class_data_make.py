import pickle as pk
import os
file_path=os.path.expanduser('~/catkin_ws/src/happymimi_voice/config')
food=["snack","bread","snack","rice"]
drink=["coke","water","tea","green tea","coffee","milk"]


with open(file_path+"/class_generalization.pkl","wb") as fl:
    dit={"food":set(food),"drink":set(drink)}
    pk.dump(dit,fl)
                       
