# Inicialmente cargamos las librerías a utilizar:
import os.path as path
import zipfile
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
from sklearn import preprocessing


rcParams['figure.figsize'] = 18, 10


# Nota: El dataset se encuentra comprimido por un tema de volumen. 
# Esta rutina chequea su existencia en formato descomprimido y lo extrae en caso de no existir. 
dataset_filename = '/usr/local/diplodatos/datos/datos-anonimizados-clientes.csv'

if path.isfile(dataset_filename) == False:
    zip = zipfile.ZipFile('/usr/local/diplodatos/datos/datos-anonimizados-clientes.zip')
    zip.extractall('/usr/local/diplodatos/datos/')
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


# Cargamos los datos nuevamente y observamos si aparece el Warning:
ventas_df = pd.read_csv("/usr/local/diplodatos/datos/datos-anonimizados-clientes.csv", dtype=ventas_df_dtype)


cant_filas = len(ventas_df)
cant_columnas = len(ventas_df.columns)

ventas_df.rename(columns={'Unnamed: 0':'indice'}, inplace=True)


ventas_df.to_csv('/usr/local/diplodatos/datos/datos-revisados-clientes.csv')

import ftfy.badness as bad

def weird(val):
    if isinstance(val, float): 
        return 0
    return bad.sequence_weirdness(val)

db_copy = ventas_df
db_copy['bad_char'] = ventas_df['ESQUEMA_COMERCIAL'].apply(weird)


# Verificamos si posee alguna linea con caracteres especiales en esa columna
db_copy[db_copy['bad_char'] > 1]
# No devolvió filas, por lo tanto no cuenta con caracteres especiales


missing_values_count = ventas_df.isnull().sum()
missing_values_count[missing_values_count > 0]

len(ventas_df.dropna())/len(ventas_df)

# son menos del 1% por lo tanto vamos a removerlas.
ventas_df = ventas_df.dropna()

# Create a label (category) encoder object
le_cat_iva = preprocessing.LabelEncoder()
le_cat = preprocessing.LabelEncoder()
le_cred_mon = preprocessing.LabelEncoder()
le_soc_jur = preprocessing.LabelEncoder()
le_estado = preprocessing.LabelEncoder()
le_mot_estado = preprocessing.LabelEncoder()
le_esq_com = preprocessing.LabelEncoder()
le_fac_cod = preprocessing.LabelEncoder()
le_uni_med = preprocessing.LabelEncoder()


# Fit the encoder to the pandas column
le_cat_iva.fit(ventas_df["CATEGORIA_IVA"])
le_cat.fit(ventas_df["CATEGORIA"])
le_estado.fit(ventas_df["ESTADO"])
le_fac_cod.fit(ventas_df["FACTURA_CODIGO"])
le_uni_med.fit(ventas_df["UNIDAD_MEDIDA"])
le_esq_com.fit(ventas_df["ESQUEMA_COMERCIAL"].astype(str))
le_mot_estado.fit(ventas_df["MOTIVO_ESTADO"].astype(str))
le_cred_mon.fit(ventas_df["CREDITO_MONEDA"].astype(str))
le_soc_jur.fit(ventas_df["SOCIEDAD_JURIDICA"].astype(str))


outliers_cantidad = ventas_df[ventas_df.CANTIDAD > 50000]
# ahora los removemos del dataset original
ventas_df = ventas_df.drop(outliers_cantidad.index)
outliers_monto_total = ventas_df[ventas_df.FACTURA_MONTO_TOTAL > 500000]
ventas_df = ventas_df.drop(outliers_monto_total.index)


outliers_apertura_adicional = ventas_df[ventas_df.APERTURA_ADICIONAL.astype(np.float) > 20]
ventas_df = ventas_df.drop(outliers_apertura_adicional.index)

ventas_df.to_csv('/usr/local/diplodatos/datos/datos-revisados-clientes.gz', compression='gzip')

ventas_df = ventas_df.sort_values(['indice', 'CODIGO_CLIENTE', 'RAZON_SOCIAL', 'CUIT', 'CATEGORIA_IVA',
       'GRUPO_CANAL', 'CANAL', 'SUBCANAL', 'APERTURA_ADICIONAL', 'CATEGORIA',
       'ZONA', 'ZONA_REPARTO', 'CONDICION_VENTA', 'CREDITO_MAXIMO',
       'CREDITO_MONEDA', 'LISTA_PRECIOS', 'AGENTE_RETENCION',
       'DIAS_TOLERANCIA_COBRO', 'GRUPO', 'SOCIEDAD_JURIDICA', 'ESTADO',
       'MOTIVO_ESTADO', 'ESQUEMA_COMERCIAL', 'FACTURA_CODIGO',
       'FACTURA_NUM_ID', 'FACTURA_SUCURSAL', 'FACTURA_FECHA',
       'FACTURA_MONTO_TOTAL', 'FACTURA_COND_VENTA', 'FACTURA_VENDEDOR',
       'CODIGO_ARTICULO', 'AGRUPACION_1', 'AGRUPACION_2', 'AGRUPACION_3',
       'AGRUPACION_4', 'AGRUPACION_5', 'AGRUPACION_6', 'CANTIDAD',
       'UNIDAD_MEDIDA', 'PRECIO_UNITARIO', 'PRECIO_TOTAL'], ascending=True )

ventas_df = ventas_df.drop(columns='ZONA_REPARTO')

ventas_df.to_csv('/usr/local/diplodatos/datos/datos-revisados-clientes.gz', compression='gzip')

print("datos-revisados-clientes.csv generado.")