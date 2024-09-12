valor = input('Ingrese su presupuesto: ')
print(type(valor))
print(valor)
bool('True') # devolverá un tipo de dato boolean
float('200.9') # devolverá un tipo de dato flotante
print(type(int(valor)))

if int(valor) >= 15000:
    print('Si puede')
else:
    print('No puede')