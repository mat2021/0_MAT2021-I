import librosa
import sys
import os
import numpy as np
import tensorflow as tf

k = 3
max_iterations = 200

#leer archivo
fileName = sys.argv[1]
y, sr = librosa.load(fileName)
partes = y.size / sr #calcula cantidad de partes

#corta
archivo = open('datosDescriptor.txt', 'w')
for parte in range(partes): #corta el audio en partes
	nombreArchivo = "parte" + '{:05d}'.format(parte) + ".wav"
	librosa.output.write_wav(nombreArchivo, y[parte*sr:(parte+1)*sr], sr)

#analizar
for parte in range(partes): #corta el audio en partes
	nombreArchivo = "parte" + '{:05d}'.format(parte) + ".wav"
	y, sr = librosa.load(nombreArchivo)
	mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
	mfccFlat = [str(item) for sublist in mfcc for item in sublist]
	archivo.write(', '.join(mfccFlat) + '\n')
archivo.close()

#clasificacion
def loadData(xs, names):
    file = open('datosDescriptor.txt', 'r')
    content = file.readlines()
    for parte in range(partes): #corta el audio en partes
    	nombreArchivo = "parte" + '{:05d}'.format(parte)
    	names.append(nombreArchivo)
    	data = content[parte].split(',')
    	data = map(float, data)
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
    results = zip(sess.run(Y), names)
    results.sort(key=lambda tup: tup[1])

    file = open("clases.txt", "w")
    for res in results:
        print("clase " + str(res[0]) + " segmento " + res[1])
        file.write(str(res[0]) + " " + str(res[1]) + "\n")
    file.close()
