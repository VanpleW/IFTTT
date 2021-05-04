'''
    import lib/dependency
'''
from face_recognition_helpers import (
    collect_face_data,
    train_face_recognizer,
    face_recognition
)

#from sensestorm import speak
import requests

'''
    start the face detection trianner, remember to comment other steps when excuting one of them
'''
# step 0: go to your phone's app store and download ifttt app

# step 1: collect face data
#collect_face_data(2,200)

# step 2: train the model
#train_face_recognizer()

# step 3: test your model with a confidence level above 80%
def action1():
#    speak('Hello Vanple')
    print('Vanple is found')
    requests.post('https://maker.ifttt.com/trigger/self_found/with/key/Bsp418bVnLsiDxt2GxdSL')

def action2():
#    speak('Hello Vanple')
    print('Yang is found')

id_name_action_list = [(1,'Vanple',action1),(2,'Yang',action2),]
face_recognition(id_name_action_list)
