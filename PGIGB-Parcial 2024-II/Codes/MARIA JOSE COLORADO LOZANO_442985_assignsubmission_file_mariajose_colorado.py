import random

def read(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]
    return datos

#def write(ruta,metodo,datos):
#    with open(ruta, metodo, encoding='utf-8') as file:
 #       for i in datos:
  #          file.write(i+'\n')


def leer_archivo(info):
    info = leer_archivo('mariajose_colorado.txt')
    info == (len(info[0].split(';')))
    return info

def lista_empleados(info):
    empleados=[]
    
    for string in info:
        parte = string.split(';')
        
        nombre = str(parte[0].split(';')[1])
        horas_contratadas = int(parte[31].split(';')[1])
        horas_trabajadas = int(parte[32].split(';')[1])

    empleado = {
        'nombre': nombre, 
        'horas_contratadas': horas_contratadas, 
        'horas_trabajadas':horas_trabajadas}
     
    empleados.append(empleado)
    return empleado

def asignar_turnos(lista_empleados):
    turnos_necesarios = {
    'C': 3,    #corridos
    'N': 3,    #nocturnos
    'PT': 1,   # post turno
    'FT': 1}     #fast track
    valor_turnos = {
        'C': 12,   # horas
        'N':12, #horas
        'PT': 6, # horas
        'FT': 6}  # horas 
    turnos_asignados = {empleado['Nombre']: [''] * 31 for empleado in lista_empleados}
    horas_trabajadas = {empleado['Nombre']: empleado['horas_trabajadas'] for empleado in lista_empleados}
    empleado = list(horas_trabajadas.keys())
    for dia in range(31):
        turnos_dia = ['C'] * valor_turnos['C'] 
        ['N'] * valor_turnos['N'] 
        ['PT'] * valor_turnos['PT'] 
        ['FT'] * valor_turnos['FT']
    random.choice(lista_empleados)
    
    for turno in turnos_dia:
            for empleado in lista_empleados:
                turno and horas_trabajadas[empleado] <= [horas_contratadas]


def main():
    info = read('mariajose_colorado.txt')
    empleados = lista_empleados(info)
    


    

if __name__ == '__main__':
    main()
    
    



    



