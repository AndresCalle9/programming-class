import os

def validar_turnos(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    dias_incompletos = []
    
    for dia in range(1, 32):
        turnos_dia = []
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            turno = datos[dia]
            if turno:
                turnos_dia.append(turno)
        
        if len(turnos_dia) != 8:
            dias_incompletos.append(dia)
    
    return dias_incompletos

def files(ruta):
    return os.listdir(ruta)

# Función principal para validar el archivo
def main():
    archivos = files('./PGIGB-Parcial-2024-II/Files')
    count = 0

    for i in archivos:
        file_name = i.split('.')[0]
        try:
            dias_incompletos = validar_turnos(f"./PGIGB-Parcial-2024-II/Files/{i}")
            
            if dias_incompletos:
                print(f"{file_name},Los siguientes días no tienen los 8 turnos necesarios: {dias_incompletos}")
            else:
                print(f"{file_name}, Todos los días tienen los 8 turnos necesarios.")
        except:
            print(f"{file_name} error")
            count += 1
    
    print(count)
        

# Ejecutar la función principal
main()
