#scope en funciones
# scope global
a = 32
print('1', a)

def example():
    # scope local
    a = 'Hola'
    print('2', a)

example()
print('3',a)

# scope en condicionales
if True:
    # scope local
    a = 42
    print('4', a)

print('5', a)

# scope en ciclos
for i in range(2):
    # scope local
    a = 52
    print('6', a)

print('7', a)


