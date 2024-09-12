# nombre = input('ingrese su nombre: ')
# peso = float(input('ingrese su peso: '))
# dosis = 200
# if peso < 100 :
#     dosis = (peso/10)*5

# print(f'el paciente {nombre} necesita una dosis de {dosis} ml del medicamento asignado')

col = [1,2,3,4,5]
row = ["a","b","c","d","e"]

arr2D = [col,row]

print(arr2D)
print(type(arr2D))

print(col)
col.append(100)
print(col)
# col.append([25,12,66,5])
print(col)
col.extend([25,12,66,5])
print(col)

col.remove(5)
print(col)

# col.pop()
# print(col)

col.pop(2)
print(col)

col[1] = 200
print(col)

idx = col.index(200)
print(idx)

col.append(200)
q = col.count(200)
print(q)

col.reverse()
print(col)

col.sort()
print(col)

#zip, concat, ones, zeros, metodos listas python