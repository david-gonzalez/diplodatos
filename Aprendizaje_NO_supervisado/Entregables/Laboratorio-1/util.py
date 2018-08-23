# Librería de rutinas para el laboratorio de Aprendizaje No Supervisado
import os.path as path
import zipfile
import pandas as pd

def check_dataset():    
    # Nota: El dataset por defecto se encuentra comprimido para reducción de volumen de almacenamiento y transferencia.
    # Esta rutina chequea su existencia en formato descomprimido y lo extrae en caso de no existir. 
    print('* Chequeando dataset de trabajo...')
    dataset_filename = './datos/datos-anonimizados-clientes.csv'
    if path.isfile(dataset_filename) == False:
        zip = zipfile.ZipFile('./datos/datos-anonimizados-clientes.zip')
        zip.extractall('./datos/')
        print('- Dataset extraido OK.')
    else:
        print('- Dataset OK.')


def load_dataset():    
    # Se carga el dataset y se lista la cantidad de registros 
    print('* Importando dataset...')
    dataset_filename = './datos/datos-anonimizados-clientes.csv'
    ventas_df = pd.read_csv(dataset_filename)
    print( len( ventas_df) + ' registros importados.')
    return ventas_df

