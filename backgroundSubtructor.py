"""
Background Subtractor

This class estimases background frame from
video files or camera streams 

"""

import cv2
import numpy as np

BGSUB_METHOD_ABSDIFF = 0
BGSUB_METHOD_MOVING_MEAN = 1
BGSUB_METHOD_XXXXX = 2

class BgSubtractor(object):
    def __init__(self, method=BGSUB_METHOD_ABSDIFF, bufferSize=10):
        """Backgorund Estimator Class
        
        Arguments:
            object {} -- 
        
        Keyword Arguments:
            method {BGSUB_METHOD} -- Background subtraction method enumator
             (default: {BGSUB_METHOD_ABSDIFF})
            bufferSize {int} -- Number of frame in frame buffer (default: {10})
        """
        # priavate varibles
        self._frameCounter = 0
        self._method = method
        self._frameBufferSize = bufferSize
        self._frameBuffer = None
        # public varibles
        self.bg = None

    def processFrame(self, frame):
        """frame processor 
        
        Arguments:
            frame {np.ndarray} -- frame to process
        
        Returns:
            np.ndarray -- frame diff with background
        """
        # init for frame 0
        if self._frameCounter == 0:
            self.bg = frame
            self._frameBuffer = np.zeros((
                self._frameBufferSize,
                frame.shape[0],
                frame.shape[1]
            ))

        # standart operations for every frame
        bufferIndex = self._frameCounter%self._frameBufferSize
        self._frameBuffer[bufferIndex,:,:] = frame
        self._frameCounter += 1

        # methods
        if self._method == BGSUB_METHOD_ABSDIFF:
            return ( frame - self.bg )
        elif self._method == BGSUB_METHOD_MOVING_MEAN:
            self.bg = np.mean(self._frameBuffer, axis=0).astype(np.uint8)           
            return ( frame - self.bg )
        elif self._method == BGSUB_METHOD_XXXXX:
            return NotImplemented