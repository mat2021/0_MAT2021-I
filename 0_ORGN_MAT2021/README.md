# ORGN_MAT2021 


## Descripción
*ORGN_MAT2021* es la versión anterior del *MAT2021*. Su objetivo  principal es llevar a cabo un análisis de señal a través de pocos   descriptores acústicos brindados por el módulo de [Librosa](https://librosa.org/)

### Procesos que realiza este código
 1. **Segmenta** el audio en trozos de 44,100 sampleos por segundo.
 2. **Analiza** cada segemento utilizando or default el Coeficientes Cepstrales de Frecuencia Mel o MFCC.
 3. **Crea** un archivo en formato TXT para guardar el análisis arrojado.
 4. **Agrupa** los arreglos numéricos obtenidos y los pone en K grupos utilizando una función de K-medios o K-means para crear los grupos correspondientes. 

### El código está ordenado de la siguiente manera:

- **1_codigos**: Códigos principales.
- **2_agrupa_Reaper**: Script creado para en el Multitrack de Reaper con el fin de distribuir los segmentos.
- **3_datos**: Los resultados que arroja el código después del análisis en este caso en formato txt.
- **4_utiles**: Varios códigos utilizados para llevar a cabo tareas útiles en la manejo de la información brindada por el código.
 
 - [ ] Más información en:
www.ottocastro.com


*@Doctorado en Tecnología Musical, UNAM. México. Noviembre, 2021. Otto Castro Solano. Agradecimiento a la beca de estudios otorgada por la Universidad de Costa Rica.*