# Author: Liang Ge
# Date: 2018-1-25
# Audio Strings LLC Copyright(c) 2018

# Record fftData from Xcode using this command:
# memory read -t float -c1024 fftData --force
# note: change 1024 to the exact fftSize (it should be half of the length of audioFrame)

import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import math
from math import pi

# Open audioFrame file and display data
fileName = 'fftData'
fileID = open(fileName, 'r')

fftData = np.empty(0)

lineStr = fileID.readline()
while lineStr != '':
	fftData = np.append(fftData, float(lineStr))
	lineStr = fileID.readline()

# Display fftData length	
print 'fftData length = ', len(fftData)

# Find the maxFrequency and its magnitude
maxIndex = 0
maxFrequencyMagnitude = fftData[maxIndex]

for i in range(1, len(fftData)):
	if fftData[i] > maxFrequencyMagnitude:
		maxIndex = i
		maxFrequencyMagnitude = fftData[maxIndex]

samplingRate = 44100
fftSize = 2048
freqBin = samplingRate / float(fftSize)
maxFrequency = maxIndex * freqBin
print 'maxFrequency = ', maxFrequency
print 'maxFrequencyMagnitude = ', maxFrequencyMagnitude

# Plot audioFrame data
plt.figure(1, figsize=(16, 8))
plt.plot(fftData)
plt.title('fftData')

plt.show()