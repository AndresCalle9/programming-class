

def read(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos=[line.strip() for line in file]
    return datos

def write(ruta, metodo, info):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in info:
            file.write(i+'\n')

def leer_archivo(datos):
    info=datos[1:]
    return info

def lista_empleados(info):
    lista = []
    for i in info:
        aux = i.split(';')
        dicc = {
            'nombre': aux[0],
            'horas_trabajadas': aux[32],
            'horas_contratadas':aux[33],
        }
        lista.append(dicc)
    return lista



#def nombres(info):
    #for i in info:
        #aux=i.split(';')
        #lisst=aux[1:]

    #return lisst

#def asignar_turnos(info,lista):
    #turnos=['C','C','C','N','N','N','FT','PT']
    #lisst=lista.append(random.choice(turnos))
    #'nombre'.key(lisst)






def main():
    archivo= read('dasha_nino.txt')
    info=leer_archivo(archivo)
    print(info)
    emp=lista_empleados(info)
    print(emp)
    #empleados=nombres(info)
    #turnos=asignar_turnos(info,empleados)
    #print(turnos)
    algo=write('dasha_nino.txt','a', ['a'] )
    print(algo)
    #archivito=write('sln.txt','w',['hola'])
    #print(archivito)
    

if __name__=='__main__':
    main()