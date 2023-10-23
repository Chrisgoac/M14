import numpy as np
import pandas as pd

url: str = "https://marcos-marva.web.uah.es/CursoSanitaria/practicas/datos/osteoporosis.csv"
df_oestop: pd.DataFrame = pd.read_csv(url, sep = "\t")

df_oestop['imc'] = pd.to_numeric(df_oestop['imc'], errors='coerce')

print('Average imc = ',df_oestop['imc'].describe().mean())

print(df_oestop['menop'].value_counts())

print(df_oestop['grupedad'].value_counts())