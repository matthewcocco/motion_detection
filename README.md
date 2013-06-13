# Python Motion Detection

----------------------------------------------------

## Usage

You'll need OpenCV, Python (I use 2.7), and a webcam.

If you've got all three of those, it should be good to go.

Please tell me if it's not.

The file you want is [ motiondetection.py ].

IMPORTANT:
    While it's running, just hit the 'q' key to quit.
    Similarly, press 'm' to toggle motion detection.

(this should run straight out of the box.)

----------------------------------------------------

## About

This tidbit of Python is (hopefully) representative of my second foray into OpenCV motion tracking.

I intend to develop something that can accurately discern humanoid motion (and will not raise false alarms for things like quick changes in lighting conditions).

Ideally, it'll be able to take a feed from a webcam in real time, highlight detected motion, and raise some sort of alarm if the motion detected appears to be humanoid - highlighting also the suspect motion in a screencap (or by emphasizing it in a video feed).

So: this will probably start with a simple `import cv` and we'll see where it goes from there.

While I know this is probably a mixture of reusing and reinventing the wheel, I feel like it is a good exercise (and will also be contributing to a personal project).

...the spec for which is quite interesting.

Did you know: `True + True = 2`?

---------------------------------

## Todo:

+ Reimplement with a nicer GUI
    + maybe get the bounding boxes to be "prettier"?
    + and/or more generally surround the motion
    + also, notify the user of 
        + the 'mode' they're in
        + uptime of the script
        + number of motion events detected since startup
+ Improve motion detection
    + slow-ish or small movements in-frame are hard to detect
        + would we be able to confuse this with camouflage?
+ Implement 'alerts'?
    + probably takes place after the nicer gui implementation


---------------------------------

I started with these very helpful copy-paste-and-play tidbits:

[https://gist.github.com/burnto/1266515][2]
[http://stackoverflow.com/questions/3374828/how-do-i-track-motion-using-opencv-in-python][3]

Yup.

---------------------------------

[1]: http://opencv.org
[2]: https://gist.github.com/burnto/1266515
[3]: http://stackoverflow.com/questions/3374828/how-do-i-track-motion-using-opencv-in-python
