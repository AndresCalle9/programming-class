import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(type(titanic))

# describir los datos
print(titanic.describe())
print(titanic['Fare'].describe())
print(titanic.head())
print(titanic.tail())

# seleccionar columnas
print(titanic['Name'])
print(titanic[['Survived','Name', 'Age']])

edad = titanic['Age']
print(edad[0], edad)
print(type(edad))

edad_arr = edad.to_numpy()
print(edad_arr)
print(type(edad_arr))
print(edad_arr.mean())

# seleccionar filas
print(titanic.iloc[100])

# filtrar
print(titanic[titanic['Survived'] == 1]['Age'].mean())