import random
def leer(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        lineas= [linea.strip() for linea in file][1:]
    return lineas

def lista_empleados(info):
    empleados_info= info
    lista_diccionarios=[]
    for linea in empleados_info:
        aux= linea.split(';')
        nombre= aux[0]
        horas_t= aux[32]
        horas_c= aux[33]
        dic={'Nombre':'','Horas_trabajadas': 0,'Horas_contratadas':0}
        while nombre not in dic['Nombre']:
            dic['Nombre']= nombre
            dic['Horas_trabajadas']= horas_t
            dic['Horas_contratadas']= horas_c
            lista_diccionarios.append(dic)
        dic={'Nombre':'','Horas_trabajadas': 0,'Horas_contratadas':0}
    return lista_diccionarios

def asignar_turnos(lista_e):
    trabajadores= lista_e
    c= 12
    n= 12
    p= 6
    f= 6
    lista_turnos=[c,n,p,f]
    for dic in trabajadores:
        lista_trabajador_turnos=[]
        cont=0
        dic_nombres_turnos={}
        nombre= dic['Nombre']
        if nombre not in dic_nombres_turnos:
            print(nombre)#------------------------------------------------------------------
            horas_contratadas= int(dic['Horas_contratadas'])
            print(horas_contratadas)#----------------------------------------
            lista_turnos_trabajador=[]
            while len(lista_turnos_trabajador) < 31:
                turno_aleatorio= random.choice(lista_turnos)
                cont += turno_aleatorio
                if cont > horas_contratadas:
                    break
                lista_turnos_trabajador.append(turno_aleatorio)
                
                print(lista_turnos_trabajador)
                if len(lista_turnos_trabajador)==31:
                    break
                print(len(lista_turnos_trabajador))
                dic_nombres_turnos[nombre]= lista_trabajador_turnos

    return dic_nombres_turnos

def escribir_archivo(ruta, mensaje):
    with open(ruta, 'a') as file:
        encabezado= f'Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas'
        file.write(encabezado + '\n')
        for i in mensaje:
            file.write(i + '\n')

def main():
    info= leer('datos.txt')
    # print(info)
    lista_empleados_v= lista_empleados(info)
    print(lista_empleados_v)
    asignar_turnos_v= asignar_turnos(lista_empleados_v)
    print(asignar_turnos_v)
    archivo_final= 'katherine_londoño.txt'
    escribir_archivo_v= escribir_archivo(archivo_final, asignar_turnos_v)

if __name__=='__main__':
    main()

