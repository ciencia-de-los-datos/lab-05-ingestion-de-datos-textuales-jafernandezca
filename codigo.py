import zipfile
import os
import pandas as pd 


directorio_actual = os.getcwd()
ruta_zip = os.path.join(directorio_actual, 'data.zip')
directorio_extraccion = directorio_actual

with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
    zip_ref.extractall(directorio_extraccion)

print("Archivo ZIP extraído con éxito.")

def generar_dataset(nombre_archivo, directorio_base):
    datos = []

    for sentimiento in os.listdir(directorio_base):
        ruta_sentimiento = os.path.join(directorio_base, sentimiento)
        if os.path.isdir(ruta_sentimiento):
            for archivo in os.listdir(ruta_sentimiento):
                ruta_archivo = os.path.join(ruta_sentimiento, archivo)
                if os.path.isfile(ruta_archivo) and archivo.endswith('.txt'):
                    with open(ruta_archivo, 'r', encoding='utf-8') as archivo_texto:
                        frase = archivo_texto.read().strip()
                        datos.append({'phrase': frase, 'sentiment': sentimiento})

    df = pd.DataFrame(datos)
    df.to_csv(nombre_archivo, index=False)
    
directorio_train = 'train'
directorio_test = 'test'

# Generar los datasets de entrenamiento y prueba
generar_dataset('train_dataset.csv', directorio_train)
generar_dataset('test_dataset.csv', directorio_test)