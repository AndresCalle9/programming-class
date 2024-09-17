def validar_turnos(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    dias_incompletos = []
    
    for dia in range(1, 32):
        turnos_dia = []
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            print(dia,datos)
            turno = datos[dia]
            if turno:
                turnos_dia.append(turno)
        
        if len(turnos_dia) != 8:
            dias_incompletos.append(dia)
    
    return dias_incompletos

# Función principal para validar el archivo
def main():
    archivo = './PGIGB-Parcial-2024-II/Files/asly.txt'
    dias_incompletos = validar_turnos(archivo)
    
    if dias_incompletos:
        print(f"Los siguientes días no tienen los 8 turnos necesarios: {dias_incompletos}")
    else:
        print("Todos los días tienen los 8 turnos necesarios.")

# Ejecutar la función principal
main()
