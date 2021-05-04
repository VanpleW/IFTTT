# SKSS SenseStorm Workshop

## Preparations

### Step 1: Download the VNC Viewer on your laptop
You could find the download link over [here](https://www.realvnc.com/en/connect/download/viewer/windows/)

Install the VNC viewer on your laptop and you should be ready to go!

### Step 2: Download the SenseStorm Robot Assistant on your phone 
_(optional if you have a phone with you)_

You could find the app by scanning the QR code:

![QR code](../main/IFTTT/support/vnc.PNG)

### Step 3: Pair your SenseStorm with the App
1. Open the App and select the tab for SenseStorm:

![step 1](../main/IFTTT/support/app1.PNG)

2. Select the Network Configuration tool:

![step 2](../main/IFTTT/support/app2.PNG)

3. Make sure your phone is connected to a WiFi, and input the WiFi password:

![step 3](../main/IFTTT/support/app3.PNG)

4. Genarate a QR code and doulbe-click the mode-selection button of the SenseStorm, the camera of sensestorm should be ON, scan the QR code with the camera until the green light of the camera is OFF.

![step 4](../main/IFTTT/support/app4.PNG)

5. You are ready to go with this IP returned!

![step 5](../main/IFTTT/support/app5.PNG)

### Step 4: Control the SenseStorm over VNC
1. Enter the IP in the top-up bar
2. username: pi
3. password: SenseStorm

## Project Detials

### Session 1, (April 13, 2021)
### Session 2, (April 20, 2021)
### Session 3, (April 27, 2021)
### Session 4, (May 4, 2021)
You could find the sensestudy codes for today [here](https://raw.githubusercontent.com/yzhang0301/codes/master/overlay.py)

#### SenseStorm Project: Facial Keypoints recognition

This project is based on detection of 64 facial keypoints on human's face. 

___Try to unlock the 64 keypoints on your face and add some animitions now!___

1. Go to the project folder by opening up the terminal and type the following commands to change directory
```
cd Desktop/sensestorm_workshop/4_facial_keypoints
```
2. Run python files by typing ttthe following. Or any other python files with the file name.
```
# python3 <file name>
# for example:
python3 ex8_image_overlay_rotation.py
```
3. You could have a look of the files inside by:
```
# sudo geany <file name> &
# for example:
sudo geany ex8_image_overlay_rotation.py &
```
