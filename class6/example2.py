lista = [1,2,3,4,5,6]

for i in lista:
    print(i**2) ## i = lista[n]

indices = range(0,len(lista))
for i in indices:
    print(lista[i]**2)


print('////////////////////')
print('////////////////////')
numeros = range(1,1001)
for i in numeros:
    if i%2 == 0:
        print(f'{i} es par')