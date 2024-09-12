dicc = {
    "nombre": "Carlos",
    "edad": 22,
    "cursos": ["Python", "Django", "JavaScript"],
    "direccion":{
        "calle": "Av. Siempre viva",
        "numero": 123
    }
}

print(type(dicc))
print(dicc['nombre'])
print(dicc['cursos'][1])
print(dicc['direccion']['calle'])

# Agregar un nuevo elemento al diccionario
dicc['telefono'] = 123456
print(dicc)
dicc['nombre'] = 'Juan'
print(dicc)

# Eliminar un elemento del diccionario
del dicc['direccion']
print(dicc)

# Recorrer un diccionario
for key, value in dicc.items():
    print(key + ":", value)

# Recorrer solo las llaves
for key in dicc.keys():
    print(key)

# Recorrer solo los valores
for value in dicc.values():
    print(value)

# Verificar si una llave existe en el diccionario
print('nombre' in dicc)
print('correo' in dicc)

# Limpiar un diccionario
# dicc.clear()
print(dicc)

# metodo get
print(dicc.get('nombre'))
print(dicc['nombre'])

# metodo setdefault
dicc['edad'] = 23
print(dicc.setdefault('estudiante', True)) #dicc['estudiante'] = True
print(dicc)

# Copiar un diccionario
dicc2 = dicc.copy()
print(dicc2)
print(dicc2 == dicc)
dicc['set'] = False
print(dicc2 == dicc)

# Crear un diccionario con llaves y valores por defecto
dicc3 = {}.fromkeys(['a', 'b', 'c'], [1,2,3])
print(dicc3)

# metodo pop
dicc.pop('nombre') # del dicc['nombre']
print(dicc)


