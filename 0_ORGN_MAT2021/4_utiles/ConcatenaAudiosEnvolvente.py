
# coding: utf-8

# In[30]:

from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import IPython.display as ipd
import librosa
import librosa.display


# In[168]:

def Split_audio(sig, samp, time_slice = 0.2):
    list_sub_signals =[]
    time_slice_samples = int(time_slice*samp)
    print("Signal sample size ",len(sig))
    print("Time slice samples ",time_slice_samples)
    num_iterations = int(len(sig)//time_slice_samples)
    print("Num boxes ",num_iterations)
    for i in range(num_iterations):
        min_index = time_slice_samples*i
        max_index = time_slice_samples*(i+1)
        #print(min_index," - ",max_index)
        list_sub_signals.append(sig[min_index:max_index])
    return list_sub_signals

def PermutarSenal(sig):
    arr = np.copy(ysplit)
    np.random.shuffle(arr)
    return arr

def AddHanning(sig):
    return sig*np.hanning(len(sig));

def AddHamming(sig):
    return sig*np.hamming(len(sig));

def SegmentsAddEnvelopeHamming(listSig):
    ysegenv = []
    winsize = len(listSig[0])
    for fragSig in listSig:
        ysegenv.append( AddHanning(fragSig))
    return ysegenv

def ConcatenateList(listSig):
    yfinal = np.array([])
    for frag in listSig:
        yfinal = np.concatenate((yfinal,frag))
    return yfinal

def PlotSignalHamming(sig):
    plt.plot(sig)
    plt.show()
    plt.plot(np.hamming(wsize))
    plt.show()
    plt.plot(AddHamming(sig))
    plt.show()


# In[171]:

# Importar audio
audio_path = 'Otto.wav'
y, sr = librosa.load(audio_path)

# Segmentamos el audio
ysplit = Split_audio(y,sr,0.1)

# Poner envolventes
yenvs = SegmentsAddEnvelopeHamming(ysplit)

# Permutamos los fragmentos
yperm = PermutarSenal(yenvs)

# Concatenar segmentos en una senal
yfinal = ConcatenateList(yperm)

# Reproducir audio final
#ipd.Audio(yfinal, rate=sr) # load a NumPy array
librosa.output.write_wav('Otto_seg.wav', yfinal, sr)

#================
# Opcionales
# PlotSignalHamming(ysplit[0])

