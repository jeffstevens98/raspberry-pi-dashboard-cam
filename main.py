"""
Raspberry Pi Car Dashboard Camera
by Jeff Stevens

This is the main code run by the raspberry pi
dashboard camera. When the car starts up, the
pi turns on. This code (main.py) immediately begins:

1. We check to see if we have enough storage space
left on the SD card to record a video of the current trip.
Enough space is defined as 1 hour of video. If we do not
have enough space, we delete the oldest video in storage
and then check again to see if we have enough space.
If we do, we continue to the next step.

2. We turn the camera on and begin recording the current trip.

3. Once the car is turned off (a signal specified by the power
from the cigarette lighter turning off), we stop recording the current
video and save it to the SD card. If there is not enough space, we delete
the oldest videos on the raspberry pi until there is enough space.

    3.5 Not part of the code, but at this point, the raspberry pi is running on an
        auxilliary power source from inside the car.
    
4. Once the video is saved, we check to see if there is a saved Wifi signal.
This saved wifi signal is intended to be the user's home network that can be
picked up from their garage or whereever they store their car. If we find a
Wifi signal, the raspberry pi communicates with a server and sends all of the videos
it has stored to the server for long term storage. The pi then deletes all of the
videos sent to the server this way.

5. Lastly, the pi turns off. Before shutting down, it sends a signal to its auxiliary
   power source to switch back to being powered by the car's cigarette lighter by default.
"""

### Libraries required ###
import picamera
import psutil

##########################

def generateFileName():
	#Take the current date and time to make a filename
	



#Welcome message
print("Raspberry Pi Dashboard Camera \n"
      "By Jeff Stevens\n\n")

#Step 1: Check to see if there is enough space to store a 1 hour video file.
print("Analyzing remaining diskspace...")
diskSpaceLeftInMB = psutil.disk_usage(".").free/1048576
minutesOfVideoRemaining = diskSpaceLeftInMB/318.75 #Found on this website: https://www.digitalrebellion.com/webapps/videocalc
'''
while remaining disk space <= amount of diskspace for 1 hour of video
    delete oldest video
'''

#Step 2: Start recording
print("Camera starting up...")
camera = picamera.PiCamera()
camera.resolution = (640,480)
#Generate name of file based on date, number of trips in day, and time
fileName = generateFileName()
camera.start_recording(fileName+ '.h264')
print("Recording has begun for " + fileName + '.h264')


#Step 3: Stop recording
#Receive signal from no power from cigarette lighter
#Change power source
camera.wait_recording(60)
camera.stop_recording()
print("Recording has stopped")
#Check to see if video is saved in directory

#Step 4: Send videos to server if wifi signal present

#Step 5: Switch power sources

