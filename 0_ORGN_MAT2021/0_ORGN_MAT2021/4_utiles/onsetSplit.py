import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

import os


y, sr = librosa.load("CIUDAD.wav")

f = open('onsets.txt', 'r')
lineasTexto = f.readlines()
f.close()

listOnset = []
for line in lineasTexto:
    onset = float(line.split("\t")[0])
    listOnset.append(int(onset*sr))

print(listOnset)

# Queremos segmentar Y de acuerdo a los valores de listOnset

listSeg = []
for i in range(len(listOnset)-1):
    limInf = listOnset[i]
    limSup = listOnset[i+1]
    segTemp = y[limInf : limSup]
    listSeg.append(segTemp)
    print("Rango: ",limInf,limSup)

#print(listSeg)
c = 0
for audio in listSeg:
    librosa.output.write_wav('./output/' +'{:05d}'.format(parte), audio, sr)
    c = c + 1