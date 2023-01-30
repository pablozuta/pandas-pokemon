import pandas as pd
import datetime as dt
import time as tm

df = pd.read_csv('pokemon_data.csv')

print(df) # muestra todos los datos del dataframe
print(df.head(30)) # esto muestra las 3 primeros raws 
print(df.tail(3)) # esto muestra las 3 ultimos raws 
print(df.columns) # muestra los nombres de las columnas
print(df['Name']) # muestra una columna en especifico
print(df['Name'] [0:15])# muestra una columna en especifico y un rango en especifico 
print(df[['Name', 'Type 1']]) # muestra varias columnas en especifico  

print(df.iloc[1]) # muestra un row en particular (iloc=integer location , aka index of the row)
print(df.iloc[0:3]) # muestra un rango de rows


# read a specific location (row and column)
print("Second Row First Column: ", df.iloc[2, 1]) # this show second row first column

# iteration
for index, row in df.iterrows():
    print(index, row)

# iteration to show the name and index only
for index, row in df.iterrows():
    print(index, row['Name'])

# find data in the dataframe
print(df.loc[df['Type 1'] == 'Fire'])   
print(df.loc[df['Type 1'] == 'Rock'])   
print(df.loc[df['Legendary'] == True])

# information standard deviation , etc
print(df.describe())

# sorting
print(df.sort_values('Name')) # alfabetical order using the values of the 'Name' column
print(df.sort_values('Name', ascending=False)) # the same but descending

# MAKING CHANGES TO THE DATA
# adding a column 'Total
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
print(df.head(5))

# deleting that column 'Total'
df = df.drop(columns=['Total'])
print(df.head(5))


#aca transformamos un array en un dataset
column = ['Mariya', 'Batman', 'Bob Esponja']
data = pd.DataFrame(column)
print(data)
print(pd.Series(column))


print(df.describe())


