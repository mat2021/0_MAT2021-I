import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

import os

#. [ [--], [--], [--], [--] ,[--] ]
#.  [  -------   ]
def ConcatenateList(listSig):
    yfinal = np.array([])
    for frag in listSig:
        yfinal = np.concatenate((yfinal,frag))
    return yfinal

#============================

listAudios = []
for file in os.listdir("./input"):
	if file.endswith(".wav"):
		print(file)
		y, sr = librosa.load("./input/"+file)
		listAudios.append(y)

print(listAudios)

listAudiosPerm = np.copy(listAudios)
np.random.shuffle(listAudiosPerm)

print("Perm")
print(listAudiosPerm)


audioOrig = ConcatenateList(listAudios)
audioFinal = ConcatenateList(listAudiosPerm)

librosa.output.write_wav('./output/Original.wav', audioOrig, sr)
librosa.output.write_wav('./output/Permutado.wav', audioFinal, sr)


