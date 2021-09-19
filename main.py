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
        auxilliary power source from inside 
    
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

#Welcome message
print("Raspberry Pi Dashboard Camera \n"
      "By Jeff Stevens\n\n")

#Step 1: Check to see if there is enough space to store a 1 hour video file.
print("Analyzing remaining diskspace...")
print(psutil.disk_usage(".").free)


camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()
