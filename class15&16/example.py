import numpy as np

a = np.array([1, 2, 3,8,9,4,5,6,7,10])
print(type(a), a)

print(a[0])

#sort
print(np.sort(a))

#concatenar
b = np.array([11,12,13])
print(np.concatenate((a,b)))

# tamaño
print(np.size(a))

# agregar elementos
a = np.append(a, [14,15,16])
print(a)

# eliminar elementos
a = np.delete(a, 0)
print(a)

np.savetxt('datos2.txt', a, fmt='%d', delimiter=',')

# slice
print(a[1:3])
print(a[1:])
print(a[:3])
print(a[3:10:2])

print(a[a>5])
print(a[a%2==0])
print(a[(a%2 == 0) | (a>5)])
print(a[(a%2 == 0) & (a>5)])

print(a.max())
print(a.min())
print(a.mean())
print(a.sum())