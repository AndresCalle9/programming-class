# leer los dias y decir que dias tienen 8 turnos y que dias no, inidicar cuales 


def leer(ruta):
    with open (ruta,'r',encoding='utf-8')as file:
        lista= [i.strip() for i in file if i.count('horas trabajadas')==0]
    return lista

def control_dias(datos):
    registro_dias_turnos_completos=[]
    registro_dias_turnos_incompletos=[]
    contador_dias = 1
    while contador_dias<=31:  
        registro_dia=[] 
        for i in datos:
            info = i.split(';')[contador_dias]
            registro_dia.append(info)
        if registro_dia.count('C')== 3 and registro_dia.count('N')==3 and registro_dia.count('PT')==1 and registro_dia.count('FT')==1 :
            registro_dias_turnos_completos.append(contador_dias)
        else:
            registro_dias_turnos_incompletos.append(contador_dias)
        contador_dias+=1
    print('a')
    return registro_dias_turnos_completos,registro_dias_turnos_incompletos


def main():
    datos = leer('asly_amado.txt')
    dias_completos, dias_incompletos= control_dias(datos)
    print('a')


if __name__=='__main__':
    main()