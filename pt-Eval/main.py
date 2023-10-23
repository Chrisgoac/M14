import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
df: pd.DataFrame = pd.read_csv('file.csv', sep = ",")

# Importació del Dataset
# 1. Explicació del context. Què son aquestes dades? Posar referències.
# Los datos vienen de el portal de datos de datos abiertos de cataluña, son los datos de las personas desaparecidas durante la guerra civil
# https://analisi.transparenciacatalunya.cat/widgets/u2ix-2jr6

# 2. Explicar les columnes.
# Id Afectat = El ID de la persona afectada en el CSV
# Sexe = El sexo de la persona desaparecida
# Municipi naixement = El municipio de nacimiento de la persona desaparecida
# Provincia naixement = La provincia de nacimiento de la persona desaparecida
# Província desaparició = La provincia en la que desapareció la persona desaparecida
# Exèrcit = Ejercito al que pertenecia la persona desaparecida
# És afusellat = Si la persona desaparecida ha sido afusellada
# Localitzat = Si se ha localziado a la persona desaparecida

# 3. Quantes files hi ha?
# El CSV cuenta con 5307 filas.
print(len(df))

# Arreglar el Dataset
# 1. El dataset està en format «tidy»? Justifiqueu la vostra resposta.
# No, ya que hay celdas en las que se especifica más de un dato, como en la columna "Lleva", que se pueden observar dos fechas.

# 2. Si no ho està, poseu-lo en aquest format.
# No será necesario ya que para lo que necesitamos el CSV no se usarán columnas que no sean tidy

# 3. Hi ha NAs? A on? Justifiqueu què fareu amb elles (esborrar-les, deixar-les, substutïr-les
# per un altre valor)




# print('Num de republicanos = ',df['Exèrcit'].avg())

republicanos = (df['Exèrcit'] == 'REPUBLICÀ').sum()
sublevados = (df['Exèrcit'] == 'REBEL').sum()
nulos = (pd.isnull(df['Exèrcit'])).sum()

# print(f'Republicanos = {republicanos}')
# print(f'Sublevados = {rebels}')
# print(f'Nulos = {nulos}')

# print(f'Total = {republicanos + sublevados + nulos}/{len(df)}')

# Etiquetas y valores para el gráfico de barras
etiquetas = ['Republicanos', 'Sublevados', 'Nulos']
valores = [republicanos, sublevados, nulos]

# Crear el gráfico de barras
plt.bar(etiquetas, valores, color=['blue', 'red', 'gray'])
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.title('Personas desaparecidas durante la guerra civil - Distribución del ejército')

# Mostrar el gráfico
# plt.show()
plt.savefig('republicanos-sublevados.png')



