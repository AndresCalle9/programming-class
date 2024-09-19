def leer_turnos_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()[1:]  
        return [linea.strip().split(';') for linea in lineas]
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no fue encontrado.')
        return []

def verificar_turnos(turnos):
    dias_correctos = []
    dias_incorrectos = []
    for dia in range(31):
        conteo_turnos = {'C': 0, 'N': 0, 'PT': 0, 'FT': 0}
        for empleado in turnos:
            turno = empleado[dia + 1] 
            if turno in conteo_turnos:
                conteo_turnos[turno] += 1

        total_turnos = sum(conteo_turnos.values())
        if total_turnos == 8:
            dias_correctos.append(dia + 1)
        else:
            dias_incorrectos.append((dia + 1, conteo_turnos))

    return dias_correctos, dias_incorrectos

def main():
    nombre_archivo = 'test.txt'
    turnos = leer_turnos_archivo(nombre_archivo)
    if not turnos:
        return
    
    dias_correctos, dias_incorrectos = verificar_turnos(turnos)
    print('Días con turnos asignados correctamente:', dias_correctos)
    print('Días con turnos asignados incorrectamente:')
    for dia, conteo in dias_incorrectos:
        print(f'Día {dia}: {conteo}')

if __name__ == '__main__':
    main()