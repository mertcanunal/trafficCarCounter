"""
Background Subtractor

This class estimases background frame from
video files or camera streams 

"""

import cv2

BGSUB_METHOD_ABSDIFF = 0
BGSUB_METHOD_XXXXX = 1

class BgSubtractor(object):
    def __init__(self, method=BGSUB_METHOD_ABSDIFF):
        self._frameCounter = 0
        self.method = method
        self.bg = None

    def processFrame(self, frame):
        if self._frameCounter == 0:
            self.bg = frame
        self._frameCounter += 1
        # methods
        if self.method == BGSUB_METHOD_ABSDIFF:
            return ( frame - self.bg )
        elif self.method == BGSUB_METHOD_XXXXX:
            return NotImplemented