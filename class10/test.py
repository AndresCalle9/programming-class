lista = range(1,11)

opt = []
j = 0
for i in lista:
    print(j,i)
    opt.append((j,i))
    j += 1
print('******************************************************')
for idx, i in enumerate(lista):
    print(idx,i)

resultado = enumerate(['a','b','c','d','e','f','g','h','i','j'])
print(list(resultado))
