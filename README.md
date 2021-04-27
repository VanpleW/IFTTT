# IFTTT Trial on SenseStorm

## Preparations

### Step 1: Download the VNC Viewer on your laptop
You could find the download link over [here](https://www.realvnc.com/en/connect/download/viewer/windows/)

Install the VNC viewer on your laptop and you should be ready to go!

### Step 2: Download the SenseStorm Robot Assistant on your phone (optional if you have a phone with you)
You could find the app by scanning the QR code:

![QR code](../main/support/vnc.PNG =400x400)

### Step 3: Pair your SenseStorm with the App
1. Open the App and select the tab for SenseStorm:

![step 1](../main/support/app1.PNG =400x400)

2. Select the Network Configuration tool:

![step 2](../main/support/app2.PNG =400x400)

3. Make sure your phone is connected to a WiFi, and input the WiFi password:

![step 3](../main/support/app3.PNG =400x400)

4. Genarate a QR code and doulbe-click the mode-selection button of the SenseStorm, the camera of sensestorm should be ON, scan the QR code with the camera until the green light of the camera is OFF.

![step 4](../main/support/app4.PNG =400x400)

5. You are ready to go with this IP returned!

![step 5](../main/support/app5.PNG =400x400)

### Step 4: Control the SenseStorm over VNC
1. Enter the IP in the top-up bar
2. username: pi
3. password: SenseStorm

## Project Trails

### Project 1: Facial Keypoints recognition
1. Go to the project folder by open up the terminal, type the following to change directory
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
### Project 2: IFTTT trial 
You need to git clone this repo on the Desktop of your SenseStorm
```
cd Desktop

git clone https://github.com/VanpleW/IFTTT.git
```
If you have a github account, please use yours to download it; Otherwise, please ask for help to me.

Then you need to open the code by:
```
cd IFTTT
sudo geany notification.py &
```
Follow the instruction inside and explore more about IFTTT on SenseStorm.
