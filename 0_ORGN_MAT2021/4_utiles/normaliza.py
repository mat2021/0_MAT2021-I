import sys
import os
import json
import csv
import pandas as pd

url = "/Users/ottocastro/Desktop/normal/datosDescriptoresTodos1.csv"
df = pd.read_csv(url, header=None)
print (df.dtypes)

df = df.set_index(1)
print (df.head())

def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

df_normalized = normalize(df).reset_index().sort_index(axis=1)
print(df_normalized)


#archivo = open("archivo.csv", "w")
#archivo.write(df_normalized)
#archivo.writelines(" 	")
#archivo.close()








