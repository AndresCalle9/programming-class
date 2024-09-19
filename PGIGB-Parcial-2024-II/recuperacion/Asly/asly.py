import random
def leer(ruta):
    with open (ruta,'r',encoding='utf-8')as file:
        lista= [i.strip() for i in file if i.count('horas trabajadas')==0]
    return lista

def lista_empleados(info):
    lista_info= []
    for i in info:
        data= i.split(';')
        dicc = { 'nombre': data[0],
                'horas_trabajadas': int(data[len(data)-2]),
                'horas_contratadas': int(data[len(data)-1])}
        lista_info.append(dicc)
    return lista_info

def asignar_turnos(info_empleados):
    dicc_final= {}
    cont_dia = 0
    while cont_dia<31:# mes
        lista_trabajadores = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        turnos_dia=['C','C','C','PT','FT','N','N','N']
        for i in range(1,9):# dia 
            turno_seleccionado=  random.choice(turnos_dia)
            if turno_seleccionado == 'C' or turno_seleccionado == 'N':
                horas_target = 12
            else:  
               horas_target= 6
            empleado_seleccionado = random.choice(lista_trabajadores)
            # cada empleado debe de tener 8 turnos por dia
            trabajador = info_empleados[empleado_seleccionado]
            while trabajador['horas_trabajadas']+horas_target >trabajador['horas_contratadas'] :
                empleado_seleccionado = random.choice(lista_trabajadores)
                trabajador = info_empleados[empleado_seleccionado]
            trabajador['horas_trabajadas'] += horas_target
            turnos_dia.remove(turno_seleccionado)
            lista_trabajadores.remove(empleado_seleccionado)
            if trabajador['nombre'] not in dicc_final.keys():
                dicc_final[trabajador['nombre']]=[]
            dicc_final[trabajador['nombre']].append(turno_seleccionado)
        # a los empleados que no seleccione mandarle '' vacios   
        for i in lista_trabajadores:
            data = info_empleados[i]
            if data['nombre'] not in dicc_final.keys():
                dicc_final[data['nombre']]=[]
            dicc_final[data['nombre']].append(' ')
        cont_dia+=1
    return dicc_final,info_empleados

def escribir(ruta,metodo,info):
    with open(ruta,metodo,encoding='utf-8')as file:
        for i in info:
            file.write(i+'\n')

def organizar(info,cuadro_turnos,info_importante):
    lista_final = []
    for idx,i in enumerate(info):
        lista_empleado= []
        nombre = i.split(';')[0]
        data =cuadro_turnos[nombre]
        lista_empleado.append(nombre)
        lista_empleado.extend(data)
        lista_empleado.append(str(info_importante[idx]['horas_trabajadas']))
        lista_empleado.append(str(info_importante[idx]['horas_contratadas']))
        info_empleado = ';'.join(lista_empleado)
        lista_final.append(info_empleado)
    escribir('asly_amado.txt','a',lista_final)
  
def main():
    info_empleados = leer('asly_amado.txt')# rectificar el nombre del txt
    list_empleados= lista_empleados(info_empleados)
    cuadro_turnos,info_importante = asignar_turnos(list_empleados)
    escribir('asly_amado.txt','w',['Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas'])
    organizar(info_empleados,cuadro_turnos,info_importante)

# leer los dias y decir que dias tienen 8 turnos y cuales no 
if __name__=='__main__':
    main()