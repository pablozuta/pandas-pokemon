import pandas as pd
import datetime as dt
import time as tm

df = pd.read_csv('pokemon_data.csv')

""" print(df) """
""" print(df.head(3))#esto muestra las 3 primeros raws """
""" print(df.tail(3))#esto muestra las 3 ultimos raws """
""" print(df.columns)#muestra los nombres de las columnas
print(df['Name'])#muestra una columna en especifico
print(df['Name'] [0:15])#muestra una columna en especifico y un rango en especifico """
""" print(df[['Name', 'Type 1']])#muestra varias columna en especifico  """

print(df.iloc[1])#muestra un row en particular
print(df.iloc[0:3])#muestra un rango de rows

#aca transformamos un array en un dataset
column = ['Mariya', 'Batman', 'Bob Esponja']
data = pd.DataFrame(column)
print(data)
print(pd.Series(column))


print(df.describe())


