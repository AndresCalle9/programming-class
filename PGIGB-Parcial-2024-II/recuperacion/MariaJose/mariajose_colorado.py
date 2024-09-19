import random

def read(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]         
    return datos

def write(ruta,metodo,datos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')




def leer_archivo(info):
    info = leer_archivo('mariajose_colorado.txt')
    info = (0,len(info[1].split(';')))
        
    return info

def lista_empleados(info):
    empleados=[]
    
    for string in info:
        col = string.split(';')
        
        nombre = str(col[0].split(';'))
        horas_contratadas = int(col[31].split(';'))
        horas_trabajadas = int(col[32].split(';'))

    empleado = {
        'nombre': nombre, 
        'horas_contratadas': horas_contratadas, 
        'horas_trabajadas':horas_trabajadas}
     
    empleados.append(empleado)
    return empleado

def asignar_turnos(lista_empleados):
    acc= 0 
    turnos_necesarios = ['C','C','C','N','N','N','PT','FT']
    valor_turnos = {
        'C': 12,   # horas
        'N':12, #horas
        'PT': 6, # horas
        'FT': 6 # horas
    } 
    acc += 1
    dia = turnos_necesarios + acc 
         
    
    horas_trabajadas = {empleado['Nombre']: valor_turnos['horas_trabajadas']*31 for empleado in lista_empleados}
    empleado = list(horas_trabajadas.keys())
    for dia in range(31):
        turnos_dia = ['C'] * valor_turnos['C'] 
        ['N'] * valor_turnos['N'] 
        ['PT'] * valor_turnos['PT'] 
        ['FT'] * valor_turnos['FT']
    random.choice(lista_empleados)
    
#    for turno in turnos_dia:
#            for empleado in lista_empleados:
#                turno and horas_trabajadas[empleado] <= [horas_contratadas]
    


def main():
    info = read('mariajose_colorado.txt')
    print(info)
    empleados = lista_empleados(info)
    print(empleados )
    asignar_turnos = lista_empleados
    print(asignar_turnos)
    write('turnos_asignados.txt','w',asignar_turnos)
    
      

if __name__ == '__main__':
    main()
    
    




    



