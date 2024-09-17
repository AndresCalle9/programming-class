import random

def read(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos=[line.strip() for line in file]
    return datos

def write(ruta,metodo,archivo):
    with open(ruta,metodo, encoding='utf-8') as file:
        for i in file:
            file.write(i+'\n')


def leer_archivo(datos):
    info=datos[1:]
    return info

def lista_empleados(datos):
    lista = []
    for i in datos:
        aux = i.split(';')
        dicc = {
            'nombre': aux[0],
            'horas_trabajadas': aux[32],
            'horas_contratadas':aux[33],
        }
        lista.append(dicc)

    return lista

#def asignar_turnos(datos):
    #for i in datos:
       #aux=i.split(';')
       #nombre=aux[i] 
       #lista_turnos=[]
       #lista_turnos.append(nombre)

      


def main():
    archivo= read('dasha_nino.txt')
    info=leer_archivo(archivo)
    print(info)
    emp=lista_empleados(info)
    print(emp)
    

if __name__=='__main__':
    main()