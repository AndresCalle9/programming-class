import random

def asignar_turnos(ayuwoki):
    f = open('santiago_ramirez.txt', 'a')
    f.write(f'\n{ayuwoki}')

def leer():
    f = open('santiago_ramirez.txt', 'r')
    print(f.readline())

def lista_empleados():
    f = open('santiago_ramirez.txt', 'a')
    f.write('Trabajando hoy:')


def main():
    lista_empleados()
    leer()
    archivo = 'santiago_ramirez.txt'

    contador = 0 
    while contador <= 8:
        numero = str(random.randint(2,16))
        puesto = random.randint(1,4)

        if puesto == 1:
            puesto = 'Corrido'

        elif puesto ==2:
            puesto='noche'

        elif puesto==3:
            puesto ='post turno'

        else:
            puesto = 'fast track'
        ayuwoki=print(f'Esclavo corporativo {numero}, va a trabajar como {puesto}')
        

        asignar_turnos(ayuwoki)
        contador +=1
    return contador

if __name__ == '__main__':
    main()