# as there are 2 operating modes in essentia which have the same algorithms,
# these latter are dispatched into 2 submodules:
from essentia.standard import *
#from essentia.streaming import *

# pylab contains the plot() function, as well as figure, etc... (same names as Matlab)
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt
import numpy as np

import sys
import os

import tensorflow as tf

# we start by instantiating the audio loader:
fileName = os.path.basename(sys.argv[1])
loader = essentia.standard.MonoLoader(filename=sys.argv[1])
# and then we actually perform the loading:
audio = loader()

w = Windowing(type = 'hann')
spectrum = Spectrum()  # FFT() would return the complex FFT, here we just want the magnitude spectrum
mfcc = MFCC()

logNorm = UnaryOperator(type='log')
mfccs = []
melbands = []
melbands_log = []
pool = essentia.Pool()
print("num de samples", len(audio))
for frame in FrameGenerator(audio, frameSize = 1024, hopSize = 512, startFromZero=True):
    mfcc_bands, mfcc_coeffs = mfcc(spectrum(w(frame)))
    pool.add('lowlevel.mfcc', mfcc_coeffs)
    pool.add('lowlevel.mfcc_bands', mfcc_bands)
    pool.add('lowlevel.mfcc_bands_log', logNorm(mfcc_bands))

minimumSegmentsLength = 4
size1 = 300
inc1 = 60
size2 = 200
inc2 = 20
cpw = 1.5
features = [val for val in pool['lowlevel.mfcc'].transpose()]
sbic = SBic(size1=size1, inc1=inc1,size2=size2, inc2=inc2,cpw=cpw, minLength=minimumSegmentsLength)
# only BIC segmentation at the moment:
segments = sbic(np.array(features))
print(segments)
cantSegmentos = len(segments) - 1

analisisData = []
for segData in range(cantSegmentos):
	inicioConcatenado = np.array([])
	for inicios in range(minimumSegmentsLength):
		inicioConcatenado = np.concatenate([inicioConcatenado,
			pool['lowlevel.mfcc'][int(segments[segData]) + inicios]])
	analisisData.append(inicioConcatenado.tolist())


k = 8
max_iterations = 600

#clasificacion
def loadData(xs, names):
    for parte in range(cantSegmentos):
    	segmento = str(parte)
    	names.append(segmento)
    	data = analisisData[parte]
    	xs.append(data)

def get_dataset():
    xs = list()
    names = list()
    loadData(xs, names)
    xs = np.asmatrix(xs)
    return xs, names

def initial_cluster_centroids(X, k):
    return X[0:k, :]

def assign_cluster(X, centroids):
    expanded_vectors = tf.expand_dims(X, 0)
    expanded_centroids = tf.expand_dims(centroids, 1)
    distances = tf.reduce_sum(tf.square(tf.subtract(expanded_vectors, expanded_centroids)), 2)
    mins = tf.argmin(distances, 0)
    return mins

def recompute_centroids(X, Y):
    sums = tf.unsorted_segment_sum(X, Y, k)
    counts = tf.unsorted_segment_sum(tf.ones_like(X), Y, k)
    return sums / counts

with tf.Session() as sess:
    sess.run(tf.local_variables_initializer())
    X, names = get_dataset()
    centroids = initial_cluster_centroids(X, k)
    i, converged = 0, False
    while not converged and i < max_iterations:
        i += 1
        Y = assign_cluster(X, centroids)
        centroids = sess.run(recompute_centroids(X, Y))
    results = sorted(zip(sess.run(Y), names), key=lambda tup: tup[1])
    #results.sort(key=lambda tup: tup[1])

    file = open("clases_" + fileName + ".txt", "w")
    file.write(os.path.abspath(sys.argv[1]) + "\n")
    file.write(str(len(audio)/44100.0) + "\n")
    
    for res in results:
        res1AsInt = int(res[1])
        inicio = segments[res1AsInt] * 512.0 / 44100
        final = segments[res1AsInt + 1] * 512.0 / 44100
        dur = final - inicio
        print("clase " + str(res[0]) + " segmento " + str(res1AsInt))
        file.write(
            str(res1AsInt) + "\t" + 
            str(res[0]) + "\t" + 
            str(inicio) + "\t" +
            str(final) + "\t" +
            str(dur) + "\t" + "\n")
    file.close()

