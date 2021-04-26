import traceback
import threading
import cv2
import os
import numpy as np
from PIL import Image

def collect_face_data(face_id, numOfImages):
    path = os.path.dirname(os.path.abspath(__file__))

    # Create the dataset folder if it does not exist
    if not os.path.exists(path + "/dataset"):
        os.makedirs(path + "/dataset")
    
    # Start capturing video 
    vid_cam = cv2.VideoCapture(0)

    # Detect object in video stream using Haarcascade Frontal Face
    face_detector = cv2.CascadeClassifier(path + '/haarcascade_frontalface_default.xml')

    # Initialize sample face image
    count = 0

    # Start looping
    while(True):
        try:
            # Capture video frame
            _, image_frame = vid_cam.read()

            # Flip the image vertically
            image_frame = cv2.flip(image_frame, 1)

            # Convert frame to grayscale
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # Detect frames of different sizes, list of faces rectangles
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            # Loops for each faces
            for (x,y,w,h) in faces:

                # Crop the image frame into rectangle
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                
                # Increment sample face image
                count += 1
                print("Captured", count, "images")
                # Save the captured image into the datasets folder
                cv2.imwrite(path + "/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                
            # Display the video frame, with bounded rectangle on the person's face
            cv2.imshow('frame', image_frame)

            # To stop taking video, press 'q' for at least 100ms
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # If image taken reach 100, stop taking video
            elif count>=numOfImages:
                break
        except :
            print( traceback.format_exc())
            break

    # Stop video
    vid_cam.release()

    # Close all started windows
    cv2.destroyAllWindows()

def train_face_recognizer():
    path = os.path.dirname(os.path.abspath(__file__)) 

    # Create the trainer folder if it does not exist
    if not os.path.exists(path + "/trainer"):
        os.makedirs(path + "/trainer")

    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Using prebuilt frontal face training model, for face detection
    detector = cv2.CascadeClassifier(path + "/haarcascade_frontalface_default.xml");

    # Create method to get the images and label data
    def getImagesAndLabels(path):

        # Get all file path
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        
        # Initialize empty face sample
        faceSamples=[]
        
        # Initialize empty id
        ids = []

        count = 0
        numOfImages = len(imagePaths) + 1
        # Loop all the file path
        for imagePath in imagePaths:
            count += 1

            # Get the image and convert it to grayscale
            PIL_img = Image.open(imagePath).convert('L')

            # PIL image to numpy array
            img_numpy = np.array(PIL_img,'uint8')

            # Get the image id
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            print("id:", id, "|\t", "progress:", round(count*100/numOfImages,2), "%")

            # Get the face from the training images
            faces = detector.detectMultiScale(img_numpy)

            # Loop for each face, append to their respective ID
            for (x,y,w,h) in faces:

                # Add the image to face samples
                faceSamples.append(img_numpy[y:y+h,x:x+w])

                # Add the ID to IDs
                ids.append(id)

        # Pass the face array and IDs array
        return faceSamples,ids



    # Get the faces and IDs
    faces,ids = getImagesAndLabels(path+ '/dataset')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    recognizer.save(path + '/trainer/trainer.yml')

    print("progress: 100 %")



im = []
faces = None
gray = None
def face_recognition(id_name_action_list, confidence_threshold=80):
    global im
    global faces
    global gray

    # Display the video frame full screen
    # cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    path = os.path.dirname(os.path.abspath(__file__)) 

    def speak(str):
        content = "espeak " + repr(str) + " 2>/dev/null"
        os.system(content)

    class FaceReconitionThread(threading.Thread):
        def __init__(self, threadID, name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

        def run(self):
            print('Starting face recognition thread')

            try:
                global im
                global faces
                global gray
                while True:
                    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                    # Get all face from the video frame
                    faces = faceCascade.detectMultiScale(gray, 1.2,5)
                    
            except:
                    print( traceback.format_exc())
                

    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained mode (takes some time)
    recognizer.read(path+'/trainer/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = path + "/haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize and start the video frame capture
    cam = cv2.VideoCapture(0)

    #init face recognition thread
    detectedFaces = []
    faces = []
    ids =[]
    prev_ids_1 = []
    prev_ids_2 = []

    gray = []
    ret, im =cam.read()


    faceRecognitionThread = FaceReconitionThread(1, "Face Reconition Thread")
    faceRecognitionThread.daemon = True
    faceRecognitionThread.start()


    # Loop
    while True:
        try:
            # Read the video frame
            ret, im =cam.read()

            prev_ids_2 = prev_ids_1
            prev_ids_1 = ids

            ids = []

            # For each face in faces
            for(x,y,w,h) in faces:

                # Create rectangle around the face
                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

                # Recognize the face belongs to which ID
                Id , confidence = recognizer.predict(gray[y:y+h,x:x+w])

                print("confidence:", confidence) 
                if confidence > confidence_threshold:
                    continue

                ids.append(Id)

                if Id  not in  prev_ids_1:
                    continue

                # Check the ID if exist 
                name = ""
                for target_ID, target_name, target_action in id_name_action_list:
                    if Id == target_ID:
                        name = target_name
                        if Id not in prev_ids_2:
                            target_action()
            

                if name == "":
                    name = "Unknown ID: " + str(Id)

                # Put text describe who is in the picture
                cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(im, str(name), (x,y-40), font, 2, (255,255,255), 3)

            cv2.imshow('window',im)


            prev_faces = faces

            # If 'q' is pressed, close program
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except:
            print( traceback.format_exc())
            break
    # Stop video
    cam.release()

    # Close all started windows
    cv2.destroyAllWindows()