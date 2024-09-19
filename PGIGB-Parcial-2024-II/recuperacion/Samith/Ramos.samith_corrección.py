import random
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        lines = file.readlines()  
        if len(lines) > 1:
            return [line.strip() for line in lines[1:]]   
        else:
            return []  
def lista_empleados(info):
    empleados = []
    for line in info:
        campos = line.split(';')
        nombre = campos[0]
        horas_trabajadas = int(campos[-2])
        horas_contratadas = int(campos[-1])
        empleados.append({
            "nombre": nombre,
            "horas_trabajadas": horas_trabajadas,
            "horas_contratadas": horas_contratadas
        })
    return empleados
def asignar_turnos(empleados):
    turnos_dia = ['C'] * 3 + ['N'] * 3 + ['PT'] * 1 + ['FT'] * 1
    turnos_dia = turnos_dia * 31  
    turnos_asignados = {}   
    for empleado in empleados:
        nombre = empleado["nombre"]
        horas_contratadas = empleado["horas_contratadas"]
        horas_trabajadas = empleado["horas_trabajadas"]       
        turnos = []
        horas_restantes = horas_contratadas - horas_trabajadas       
        for _ in range(31):
            if horas_restantes <= 0:
                turnos.append('Libre')
                continue           
            turno = random.choice(turnos_dia)
            if turno == 'C' or horas_restantes >= 12:
                turnos.append(turno)
                horas_restantes -= 12
            elif turno == 'N' or horas_restantes >= 12:
                turnos.append(turno)
                horas_restantes -= 12
            elif turno == 'PT' or horas_restantes >= 6:
                turnos.append(turno)
                horas_restantes -= 6
            elif turno == 'FT' or horas_restantes >= 6:
                turnos.append(turno)
                horas_restantes -= 6
            else:
                turnos.append('Libre')
        
        turnos_asignados[nombre] = turnos
    
    return turnos_asignados

def escribir_archivo(nombre_archivo, empleados, turnos_asignados):
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write("Nombre ; Turnos ; Horas Trabajadas ; Horas Contratadas\n")
        for empleado in empleados:
            nombre = empleado["nombre"]
            turnos = turnos_asignados.get(nombre, [])
            turnos_str = ';'.join(turnos)
            horas_trabajadas = empleado["horas_trabajadas"]
            horas_contratadas = empleado["horas_contratadas"]
            file.write(f"{nombre};{turnos_str};{horas_trabajadas};{horas_contratadas}\n")

def main():
    info = leer_archivo('asly_amado.txt')
    print('++++++LISTA DE EMPLEADOS++++++')
    print(info)
    empleados = lista_empleados(info)
    print('++++++ASIGNACIONES++++++')
    print(empleados)
    cuadro_turnos = asignar_turnos(empleados)
    print('++++++TURNOS+++++++')
    print(cuadro_turnos)
    actualizar = escribir_archivo('samith.ramos.txt', empleados, cuadro_turnos)
    print(actualizar)

if __name__ == '__main__':
    main()



#realizar una funcion mas para identificar a los trabajadores que tengan 8 dias libres

import random
def read(ruta):
    with open(ruta, 'r', encoding= 'uft-8') as file:
        output = [i.strip() for i in file]
    output.pop(0)

    return output

def list_dicc(info):
    output = []
    for i in info:
        aux = i.split(';')
        output.append({
            'nombre': aux[0],
            'horas_trabajadas': int(aux[32]),
            'horas_contratadas': int(aux[33])
        })
    return output

def cuadro_turnos(usuarios):
    output = {empleado['nombre']:['']*31 for empleado in usuarios}
    turnos_dicc = {
        'C': 12,
        'N': 12,
        'PT': 6,
        'FT': 6
    }
    for dia in range(31):
        turnos = ['C','C','C','N','N','N','PT','FT']
        for turno in turnos:
            asignado = False
            intento = 0
            while not asignado and intento < len(usuarios):
                elegido = random.choice(usuarios)
                horas_trabajadas = elegido['horas_trabajadas']
                if horas_trabajadas + turnos_dicc[turno] < elegido['horas_trabajadas'] and output:
                    output[elegido['nombre']][dia] = turno
                    elegido['horas_trabajadas'] += turnos_dicc[turno]
                    asignado = True
                intento += 1
            
    return output

def write(ruta,datos,metodo):
    with open(ruta,metodo, encoding= 'uft-8') as file:
        for i in datos:
            file.write(i + '\n')
def main():

    datos = read('asly_amado.txt')
    print(datos)
    usuarios = list_dicc()
    turnos = cuadro_turnos(usuarios)
    print(turnos)


if __name__ == '__main__':
    main()


# la idea es crear un nuevo archivo llamado 8 dias.txt donde se adicionen los empleados que tienen los 8 dias libres

