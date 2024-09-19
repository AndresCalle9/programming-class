import random
def lee_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos = [i.strip().split(';') for i in file]
        datos.pop(0)
    return datos

def lista_empleados(info):
    lista = []
    
    for i in info:
        aux2 = i[32]
        aux3 = i[33]
        aux1 =i[0]
        dicc = {
            'nombre': aux1,
            'horas contratadas': int(aux2),
            'horas trabajadas': int(aux3)
        }
        lista.append(dicc)
    return lista

def asignar_turnos(empleado):
    dicc = {
        'C': 3,
        'N': 3,
        'PT': 1,
        'FT': 1
    }
    dicc1 = {
    }
    for i in empleado:
        print(i)
        

def escribir_archivos(ruta, metodo, cuadro_turnos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in cuadro_turnos:
            file.write(cuadro_turnos)


def main():
    ruta = 'sebastian_gutierrez.txt'
    info = lee_archivo(ruta) 
    print('hola')

    empleado = lista_empleados(info)
    print(empleado)
    cuadro_turnos = asignar_turnos(empleado)
    escribir_archivos('test.txt', 'a', cuadro_turnos)
    #archivo que valide que la solucion esta bien 
if __name__ == '__main__':
    main()