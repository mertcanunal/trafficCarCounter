
import cv2
import numpy as np
from backgroundSubtructor import BgSubtractor, BGSUB_METHOD_ABSDIFF

def toGray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

bgSub = BgSubtractor(method=BGSUB_METHOD_ABSDIFF)
cap = cv2.VideoCapture('data/Cars - 1900.mp4')

if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

        # Display the resulting frame
        cv2.imshow('Frame', bgSub.processFrame(frame))

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

    lastFrame = frame



# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
