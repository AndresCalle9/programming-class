def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding= 'utf-8') as archivo:
            lineas = archivo.readlines()
        return lineas[1:] if len(lineas) > 1 else []
    
    except Exception as e:
        return f'Ocurrió un error al leer el archivo: {e}'
    
def lista_empleados(lineas_archivo):    
    empleados = []
    for linea in lineas_archivo:
        partes = linea.strip().split(';')
        nombre = partes[0]
        horas_trabajadas = int(partes[-2])
        horas_contratadas = int(partes[-1])
        empleados.append({
            'nombre': nombre,
            'horas_trabajadas': horas_trabajadas,
            'horas_contratadas': horas_contratadas
        })
    
    return empleados

def asignar_turnos(lista_empleados):
    turnos_dia = ['C', 'C', 'C', 'N', 'N', 'N', 'PT', 'FT']
    turnos_asignados = {empleado['nombre']: ['']*31 for empleado in lista_empleados}
    
    empleados = {empleado['nombre']: {
        'horas_contratadas': empleado['horas_contratadas'],
        'horas_trabajadas': 0
    } for empleado in lista_empleados}
    
    num_empleados = len(lista_empleados)
    empleados_lista = list(empleados.keys())
    
    for dia in range(31):
        descansando_idx = set(range(dia * 7 % num_empleados, (dia + 1) * 7 % num_empleados))
        empleados_dia = [empleado for i, empleado in enumerate(empleados_lista) if i not in descansando_idx]
        empleados_dia.sort()      
        for i, turno in enumerate(turnos_dia):
            horas_turno = 12 if turno in ['C', 'N'] else 6
            empleado_idx = i % len(empleados_dia)
            empleado = empleados_dia[empleado_idx]
            
            if empleados[empleado]['horas_trabajadas'] + horas_turno <= empleados[empleado]['horas_contratadas']:
                turnos_asignados[empleado][dia] = turno
                empleados[empleado]['horas_trabajadas'] += horas_turno
            else:
                for j in range(empleado_idx + 1, empleado_idx + len(empleados_dia)):
                    empleado = empleados_dia[j % len(empleados_dia)]
                    if empleados[empleado]['horas_trabajadas'] + horas_turno <= empleados[empleado]['horas_contratadas']:
                        turnos_asignados[empleado][dia] = turno
                        empleados[empleado]['horas_trabajadas'] += horas_turno
                        break
    
    return turnos_asignados

def escribir_archivo(nombre_archivo, lista_empleados, diccionario_turnos):
    try:
        with open(nombre_archivo, 'w', encoding= 'utf-8') as archivo:
            encabezado = 'Nombre;' + ';'.join(f'{i+1}' for i in range(31)) + ';Horas Trabajadas;Horas Contratadas\n'
            archivo.write(encabezado)
            
            for empleado in lista_empleados:
                nombre = empleado['nombre']
                horas_trabajadas = empleado['horas_trabajadas']
                horas_contratadas = empleado['horas_contratadas']
                
                turnos = diccionario_turnos.get(nombre, [])
                linea = f'{nombre};' + ';'.join(turnos) + f';{horas_trabajadas};{horas_contratadas}\n'
                archivo.write(linea)
        
        return f"Archivo '{nombre_archivo}' escrito con éxito."
    
    except Exception as e:
        return f'Ocurrió un error al escribir el archivo: {e}'
    
def main():
    archivo_entrada = 'sofia_aguilar.txt'
    archivo_salida = 'test.txt'
    lineas = leer_archivo(archivo_entrada)
    if isinstance(lineas, str): 
        print(lineas)
        return
      
    empleados = lista_empleados(lineas)
    cuadro_turnos = asignar_turnos(empleados)
    resultado = escribir_archivo(archivo_salida, empleados, cuadro_turnos)
    print(resultado)

if __name__ == '__main__':
    main()