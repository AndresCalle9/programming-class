def read(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]
    return datos

def write(ruta,metodo, datos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')




def leer_archivo(datos):
    lista = []
    for fila in range(1,len(datos)):
        aux = datos[fila]
        lista.append(aux)

    return lista
            

def lista_empleados(datos):
    lista = []
    for i in datos:
        aux = i.split(';')
        dicc  = {
            'nombre':aux[0],
            'horas_trabajadas':aux[-2],
            'horas_contratadas': aux[-1]
        }
      
        lista.append(dicc)
    
    return lista 

def asignar_turnos(datos):
    dicc = {}
    for fila in datos:
        dicc[fila['nombre']] = [' ' for i in range(0,32)]

        
    return dicc


def main():
    info = read('jesus_dehoyos.txt')
    mostrar = leer_archivo(info)
    print(mostrar)
    empleados = lista_empleados(mostrar)
    print(empleados)
    turnos = asignar_turnos(empleados)
    print(turnos)



if __name__ == '__main__':
    main()

