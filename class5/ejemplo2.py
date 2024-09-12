kamila = 18
edad = 18
votacion = 21

if kamila >= edad:
    print('Kamila es mayor de edad')
else:
    print('Kamila no es mayor de edad')

if kamila >= votacion:
    print('Kamila puede votar')
else:
    print('kamila no puede votar')

if (kamila >= edad) and (kamila >= votacion):
    print('Kamila es mayor de edad y puede votar')
elif kamila >= edad:
    print('mayor de edad')
elif kamila < votacion:
    print('kamila no puede votar')
else:
    print('ups error')


if kamila == 20:
    print('es 20')

if kamila == 19:
    print('es 19')
else:
    print('no es 19')
