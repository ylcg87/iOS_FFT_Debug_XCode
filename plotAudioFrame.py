# Author: Liang Ge
# Date: 2018-1-25
# Audio Strings LLC Copyright(c) 2018

# Record data from Xcode using this command:
# memory read -t float -c2048 &audioFrame[0] --force
# note: change 2048 to the exact audioFrame length

import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import math
from math import pi

# Open audioFrame file and display data
fileName = 'audioFrame'
fileID = open(fileName, 'r')

audioFrame = np.empty(0)

lineStr = fileID.readline()
while lineStr != '':
	audioFrame = np.append(audioFrame, float(lineStr))
	lineStr = fileID.readline()
	
print 'audioFrame length = ', len(audioFrame)