import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
df: pd.DataFrame = pd.read_csv('file.csv', sep = ",")

# print('Num de republicanos = ',df['Exèrcit'].avg())

republicanos = (df['Exèrcit'] == 'REPUBLICÀ').sum()
rebels = (df['Exèrcit'] == 'REBEL').sum()
nulos = (pd.isnull(df['Exèrcit'])).sum()

print(f'Republicanos = {republicanos}')
print(f'Rebels = {rebels}')
print(f'Nulos = {nulos}')

print(f'Total = {republicanos + rebels + nulos}/{len(df)}')

# print(df.head())

# Etiquetas y valores para el gráfico de barras
etiquetas = ['Republicanos', 'Rebeldes', 'Nulos']
valores = [republicanos, rebels, nulos]

# Crear el gráfico de barras
plt.bar(etiquetas, valores, color=['blue', 'red', 'gray'])
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.title('Personas desaparecidas durante la guerra civil - Distribución del ejército')

# Mostrar el gráfico
# plt.show()
plt.savefig('republicanos-rebel.png')



