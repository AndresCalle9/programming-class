import random

def read(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        datos=[i.strip() for i in file if 'Nombre'not in i]
    return datos

def write(ruta,metodo,datos):
    with open(ruta,metodo,encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')

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

def asignar_turnos(dic_empleados,info):
    dicc_turnos={}
    turnos=['C','N','FT','PT','V']
    turno_por_dia=[]
    conta=0
    for col in range(1,len(info[1].split(';'))):
        conta=0
        for fila in range(0,len(info)):
            aux=info[conta].split(';')
            choice=random.choice(turnos)
            aux[col]=choice
            turno_por_dia.append(choice)
            if choice=='C' or choice=='N':
                if turno_por_dia.count(choice)>3:
                    aux[col]='V'
            elif choice=='FT' or choice=='PT':
                if turno_por_dia.count(choice)>1:
                    aux[col]='V'
            info[fila]=';'.join(aux)
            conta+=1
     
        

def main():
    archivo='empleados.txt'
    info=read(archivo)
    dic_empleados=lista_empleados(info)
    dic_turnos=asignar_turnos(dic_empleados,info)




if __name__=='__main__':
    main()