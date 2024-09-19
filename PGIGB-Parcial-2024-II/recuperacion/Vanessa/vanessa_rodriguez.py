import random

def read(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        datos=[i.strip() for i in file if 'Nombre'not in i]
    return datos

def write(archivo,empleados,turnos_asig,info):
    with open(archivo,'w',encoding='utf-8') as file:
        conta_dos=0
        lis_emple=[i['Nombre'] for i in empleados]
        for col in range(1,len(info[1].split(';'))):
            conta=0
            conta_dos=0
            for fila in range(0,len(info)):
                aux=info[conta].split(';')
                aux[col]=turnos_asig[lis_emple[fila]][conta_dos]
                info[fila]=';'.join(aux)
                conta+=1
    
    return info
    


def lista_empleados(info):
    lis_dic=[]
    for emp in info:
        emp_dicc={}
        aux=emp.split(';')
        emp_dicc['Nombre']=aux[0]
        emp_dicc['horas trabajadas']=int(aux[32])
        emp_dicc['horas contraradas']=int(aux[33])
        lis_dic.append(emp_dicc)
    return lis_dic

def asignar_turnos(dic_empleados,):
    dicc_turnos={i['Nombre']:['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''] for i in dic_empleados}
    lista_emplead=[i['Nombre'] for i in dic_empleados]
    turnos=['C','C','C','FT','N','N','N','PT',' ',' ',' ',' ',' ',' ',' ']
    escogidos=[]
    cont=0
    while cont<31:
        for i in range(1,15):
            empleado=random.choice(lista_emplead)
            if empleado not in escogidos:
                dicc_turnos[empleado][cont]=turnos[i]
                escogidos.append(empleado)
        cont+=1
        escogidos=[]
    return dicc_turnos

            
# que valide que dias tienen 8 turnos y que dias tiene mas 

def main():
    archivo='vanessa_rodriguez.txt'
    info=read(archivo)
    dic_empleados=lista_empleados(info)
    dic_turnos=asignar_turnos(dic_empleados)
    print(dic_turnos)
    hola =write('test.txt',dic_empleados,dic_turnos,info)
    for i in hola:
        print(i)
    




if __name__=='__main__':
    main()