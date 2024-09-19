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
    dic_turnos={}
    c= 12
    n= 12
    p= 6
    f= 6
    lista_turnos=[c,n,p,f]
    lista_turnos_vacios=['']*31
    for dic in trabajadores:
        nombres= dic['Nombre']
        if nombres not in dic_turnos:
            dic_turnos[nombres]= lista_turnos_vacios
            turno= random.choice(lista_turnos)
            # dic_turnos[nombres]= turno
   
    return dic_turnos

def escribir_archivo(ruta, metodo, asignar_turnos):
    with open(ruta, metodo, encoding='utf-8') as file:
        encabezado=f'Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas'
        file.write(encabezado)
        for i in asignar_turnos:
            file.write(i + '\n')

def main():
    archivo= 'katherine_londoño_rua.txt'
    info= leer(archivo)
    # print(info)
    lista_empleados_v= lista_empleados(info)
    print(lista_empleados_v)
    asignar_turnos_v= asignar_turnos(lista_empleados_v)
    print(asignar_turnos_v)
    escribir_archivo_v= escribir_archivo(archivo, 'w', asignar_turnos_v)

if __name__=='__main__':
    main()