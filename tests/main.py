import numpy as np
import pandas as pd
import os.path
from urllib.request import urlretrieve
url: str = "https://marcos-marva.web.uah.es/CursoSanitaria/practicas/datos/osteoporosis.csv"
csv_file:str = "nou_oestoporisi.csv"
if not os.path.isfile(csv_file):
    urlretrieve(url,csv_file)
# Llegim dataframe, separador fitxers \t, acceptem la primera columna com a index.
col_list: list[str] = ['registro','area','edad','imc','bua','clasif','edad_men','menop','tipo_men']
df_oestop: pd.DataFrame = pd.read_csv(url, sep = "\t")
print(df_oestop.describe())

# Sobreescrivim el dataframe.
df_oestop = pd.DataFrame(df_oestop,columns=col_list)

# Es bo saber el nom i tipus de cada columna.
print(df_oestop.dtypes)

# Provem algunes funcions útils.
print('Max edad = ',df_oestop['imc'].avg())

# print(df_oestop['menop']=='NO')
# Quins possibles valors tenim per a la columna ?
print(df_oestop['menop'].value_counts())

# Si només volem saber qui no té menopausia.
# print(df_oestop['menop'].value_counts()['NO'])

# Ja podem guardar el nou fitxer si volem
df_oestop.to_csv(ruta_nou_fitxer, sep = "\t", index=False) 