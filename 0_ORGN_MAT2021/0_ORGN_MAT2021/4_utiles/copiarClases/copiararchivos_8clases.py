# copiar archivos
import shutil, os


f=open('texto.txt',"r")
lines=f.readlines()
f.close()

result=[]
for x in lines:
	splits = x.split(' ')
	if len(splits)==2:
		clase =int(splits[0])
		nombreArchivo = splits[1].strip()+".wav"
		print(clase)
		print(nombreArchivo)
		result.append(clase)
		# Aqui haces las copias
		if clase == 0:
			print('Copiar archivo a folder 0')
			shutil.copy(nombreArchivo, 'clase_0')
		if clase == 1:
			print('Copiar archivo a folder 1')
			shutil.copy(nombreArchivo, 'clase_1')
		if clase == 2:
			print('Copiar archivo a folder 2')
			shutil.copy(nombreArchivo, 'clase_2')
		if clase == 3:
			print('Copiar archivo a folder 3')
			shutil.copy(nombreArchivo, 'clase_3')
		if clase == 4:
			print('Copiar archivo a folder 4')
			shutil.copy(nombreArchivo, 'clase_4')
		if clase == 5:
			print('Copiar archivo a folder 5')
			shutil.copy(nombreArchivo, 'clase_5')
		if clase == 6:
			print('Copiar archivo a folder 6')
			shutil.copy(nombreArchivo, 'clase_6')
		if clase == 7:
			print('Copiar archivo a folder 7')
			shutil.copy(nombreArchivo, 'clase_7')
		if clase == 8:
			print('Copiar archivo a folder 8')
			shutil.copy(nombreArchivo, 'clase_8')


