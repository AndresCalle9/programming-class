import random
def lee_archivo(ruta):
    datos2 = []
    with open(ruta, 'r', encoding='utf-8') as file:
        datos = [i.strip().split(';') for i in file]
        for i in range(1, len(datos)):
            aux = datos[i]
            for j in aux:
                datos2.append(j)
    return datos2

def lista_empleados(info, info2):
    dicc = {
        'nombre': '',
        'horas contratadas':'',
        'horas trabajadas': ''
    }

    for i in range(1,len(info2)):
        aux = info2[i]
        for j in aux:
            aux2 = j
            dicc['nombre'] += aux2
            dicc['horas contratadas'] = j

    


def main():
    ruta = 'sebastian_gutierrez.txt'
    info = lee_archivo(ruta) 
    print(info)
    print('hola')

    #empleado = lista_empleados(info, info2)
    #print(empleado)
if __name__ == '__main__':
    main()