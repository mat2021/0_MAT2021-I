import numpy as np
import librosa
import librosa.display
import os

y, sr = librosa.load("totalaudio.wav", sr=44100)

f = open('onsets.txt', 'r')
lineasTexto = f.readlines()
f.close()


listOnset = []
for line in lineasTexto:
    onset = float(line.split("\t")[0])
    listOnset.append(int(onset*sr))

print(listOnset)

listSeg = []
for i in range(len(listOnset)-1):
    limInf = listOnset[i]
    limSup = listOnset[i+1]
    segTemp = y[limInf : limSup]
    listSeg.append(segTemp)
    print("Rango: ",limInf,limSup)

n= 0
c = 0
for audio in listSeg:
    librosa.output.write_wav('./output/' +'{:05d}'.format(c)+ ".wav", audio, sr)
    c = c + 1






