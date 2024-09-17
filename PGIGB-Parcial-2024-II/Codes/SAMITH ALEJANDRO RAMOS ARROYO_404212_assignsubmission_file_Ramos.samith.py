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


 