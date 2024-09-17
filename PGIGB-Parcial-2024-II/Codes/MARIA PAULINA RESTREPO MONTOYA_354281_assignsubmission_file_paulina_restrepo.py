import random

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file if line.count('Nombre') != 1]
        return datos

def lista_empleados(datos):
    empleados = []
    for linea in datos:
        partes = linea.split(';')
        nombre = partes[0]
        horas_trabajadas = int(partes[-2])
        horas_contratadas = int(partes[-1])
        empleados.append({
            "nombre": nombre,
            "horas_trabajadas": horas_trabajadas,
            "horas_contratadas": horas_contratadas
        })
    return empleados

def asignar_turnos(empleados):
    turnos_necesarios = ['C'] * 3 + ['N'] * 3 + ['PT'] + ['FT']
    asignaciones = {empleado['nombre']: [''] * 31 for empleado in empleados}

    for dia in range(31):
        empleados_disponibles = [e for e in empleados if e['horas_contratadas'] - e['horas_trabajadas'] > 0]
        turnos_dia = turnos_necesarios[:]

        while turnos_dia and empleados_disponibles:
            turno = turnos_dia.pop(0)
            horas_requeridas = 12 if turno in ['C', 'N'] else 6

            empleados_con_horas = [e for e in empleados_disponibles if e['horas_contratadas'] - e['horas_trabajadas'] >= horas_requeridas]

            if empleados_con_horas:
                empleado = random.choice(empleados_con_horas)
                nombre = empleado['nombre']
                asignaciones[nombre][dia] = turno
                empleado['horas_trabajadas'] += horas_requeridas

                if empleado['horas_contratadas'] - empleado['horas_trabajadas'] < 6:
                    empleados_disponibles.remove(empleado)

    return asignaciones

def escribir_archivo(ruta, empleados, turnos):
    with open(ruta, 'w', encoding='utf-8') as file:
        file.write("Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas\n")
        for empleado in empleados:
            nombre = empleado['nombre']
            asignacion_dias = turnos[nombre]
            horas_trabajadas = empleado['horas_trabajadas']
            horas_contratadas = empleado['horas_contratadas']
            linea = f"{nombre};" + ";".join(asignacion_dias) + f";{horas_trabajadas};{horas_contratadas}\n"
            file.write(linea)

def main():
    info = leer_archivo('datos.txt')
    empleados = lista_empleados(info)
    cuadro_turnos = asignar_turnos(empleados)
    escribir_archivo('paulina_restrepo.txt', empleados, cuadro_turnos)

if __name__== '__main__':
    main()

  