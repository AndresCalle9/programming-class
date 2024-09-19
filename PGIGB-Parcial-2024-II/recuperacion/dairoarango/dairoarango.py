import random
def leer(ruta, target):
    with open(ruta, 'r', encoding='utf-8') as file:
        lista = [i.strip() for i in file if i.count(target) == 0]
    return lista

def lista_de_empleados(info):
    empleados = []
    for i in info:
        aux = i.split(';')
        nombre = aux[0]
        horas_trabajadas = int(aux[32])
        horas_contratadas = int(aux[33])
        empleados.append({
            'Nombre': nombre,
            'Horas_trabajadas': horas_trabajadas,
            'Horas_contratadas': horas_contratadas
        })
    return empleados

def asignar_turnos(empleados):
    tipos_turnos = ['C', 'C', 'C', 'N', 'N', 'N', 'PT', 'FT']
    turnos_asignados = {empleado['Nombre']: ['DESCANSA'] * 31 for empleado in empleados}
    horas_trabajadas = {empleado['Nombre']: empleado['Horas_trabajadas'] for empleado in empleados}
    for dia in range(31):
        random.choice(tipos_turnos)
        for turno in tipos_turnos:
            if turno in ['C', 'N']:
                turno_horas = 12 
            else:
                turno_horas= 6
            empleados_disponibles = [
                empleado for empleado in empleados
                if horas_trabajadas[empleado['Nombre']] + turno_horas <= empleado['Horas_contratadas']]
            if empleados_disponibles:
                empleado = random.choice(empleados_disponibles)
                nombre = empleado['Nombre']
                for i in range(31):
                    if turnos_asignados[nombre][i] == 'DESCANSA':
                        turnos_asignados[nombre][i] = turno
                        horas_trabajadas[nombre] += turno_horas
                        break
    return turnos_asignados

def escribir(ruta,empleados, turnos_asignados):
    with open(ruta,'w', encoding='utf-8') as file:
        file.write('Nombre;Turnos;Horas_trabajadas;Horas_contratadas\n')
        for empleado in empleados:
            nombre = empleado['Nombre']
            turnos = ' '.join(turno for turno in turnos_asignados.get(nombre, []))
            horas_trabajadas = 0
            for turno in turnos_asignados.get(nombre, []):
                if turno == 'C' or turno == 'N':
                    horas_trabajadas += 12
                elif turno == 'PT' or turno == 'FT':
                    horas_trabajadas += 6
            horas_contratadas = empleado['Horas_contratadas']
            file.write(f'{nombre};{turnos};{horas_trabajadas};{horas_contratadas}\n')

def main():
    archivo = leer('test.txt','Nombre')
    empleados = lista_de_empleados(archivo)
    for i in empleados:
        print(i)
    turnos_asignados = asignar_turnos(empleados)
    print(turnos_asignados)
    escribir('turnos_asignados.txt', empleados,turnos_asignados)

if __name__ == '__main__':
    main() 
 