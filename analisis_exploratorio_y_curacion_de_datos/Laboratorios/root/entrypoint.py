import os.path as path
import zipfile
import pandas as pd
import numpy as np
import seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Nota: El dataset se encuentra comprimido por un tema de volumen. 
# Esta rutina chequea su existencia y lo extrae en caso de no existir. 
dataset_filename = '../datos/datos-anonimizados-clientes.csv'

if path.isfile(dataset_filename) == False:
    zip = zipfile.ZipFile('./datos/datos-anonimizados-clientes.zip')
    zip.extractall('./datos/')
    print('Dataset extraido. Continuamos.')
else:
    print('El dataset existe. Continuamos.')

ventas_df_dtype={'CODIGO_CLIENTE': object,
 'RAZON_SOCIAL':  object,
 'CUIT': object,
 'CATEGORIA_IVA': object,
 'GRUPO_CANAL': object,
 'CANAL': object,
 'SUBCANAL': object,
 'APERTURA_ADICIONAL': object,
 'CATEGORIA': object,
 'ZONA': object,
 'ZONA_REPARTO': object,
 'CONDICION_VENTA': object,
 'CREDITO_MAXIMO': np.dtype('f'),
 'CREDITO_MONEDA': object,
 'LISTA_PRECIOS': object,
 'AGENTE_RETENCION': np.dtype('?'),
 'DIAS_TOLERANCIA_COBRO': np.dtype('i'),
 'GRUPO': object,
 'SOCIEDAD_JURIDICA': object,
 'ESTADO': object,
 'MOTIVO_ESTADO': object,
 'ESQUEMA_COMERCIAL': object,
 'DIRECCION_CALLE': object,
 'DIRECCION_NUMERO': object,
 'CODIGO_POSTAL': object,
 'LATITUD': np.dtype('f'),
 'LONGITUD': np.dtype('f') ,
 'DIRECCION_PRINCIPAL': object,
 'FACTURA_CODIGO': object,
 'FACTURA_NUMERO': np.dtype('i'),
 'FACTURA_SUCURSAL': np.dtype('i'),
 'FACTURA_FECHA': object,
 'FACTURA_MONTO_TOTAL': np.dtype('f'),
 'FACTURA_COND_VENTA': object,
 'FACTURA_VENDEDOR': object,
 'CODIGO_ARTICULO': object,
 'DESCRIPCION': object,
 'AGRUPACION_1': object,
 'AGRUPACION_2': object,
 'AGRUPACION_3': object,
 'AGRUPACION_4': object,
 'AGRUPACION_5': object,
 'AGRUPACION_6': object,
 'CANTIDAD': np.dtype('d'),
 'UNIDAD_MEDIDA': object,
 'PRECIO_UNITARIO': np.dtype('d'),
 'PRECIO_TOTAL' : np.dtype('d')}

ventas_df = pd.read_csv("./datos/datos-anonimizados-clientes.csv", dtype=ventas_df_dtype)

print("Hola Mundo")
