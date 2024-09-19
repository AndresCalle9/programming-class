import random

def leer_archivo(kamila_urrego):
    with open(kamila_urrego, 'r') as archivo:
        lineas = archivo.readlines()
    
    return [linea.strip() for linea in lineas[1:]]


def lista_empleados(lista_strings):
    empleados = []
    for linea in lista_strings:
        espacios = linea.split(';')
        nombre = espacios[0]
        hor_trabaj = int(espacios[-2])
        hor_contra = int(espacios[-1])
        empleados.append({
            "nombre": nombre,
            "hor_trabaj": hor_trabaj,
            "hor_contra": hor_contra
        })
    return empleados 

def asignacion_turnos(empleado):
    turnos_dia = ('C', 'C', 'C', 'N', 'N', 'N', 'PT', 'FT')
    dias_mes = 31
    turnos= ()

    turnos(empleado("nombre")) == None* dias_mes 
    hor_trabaj= 0
    hor_contra= empleado ("hor_contra")

    for dia in range(dias_mes):
            if hor_trabaj >= hor_contra:
                break
            
            turno = random.choice(turnos_dia)
            if turno == "C":
                if hor_trabaj + 12 <= hor_contra:
                    turnos(empleado("nombre"))(dia) == "C"
                    hor_trabaj += 12
            elif turno == "N":
                if hor_trabaj + 12 <= hor_contra:
                    turnos(empleado("nombre"))(dia) == "N"
                    hor_trabaj += 12
            elif turno == "PT":
                if hor_trabaj + 6 <= hor_contra:
                    turnos(empleado("nombre"))(dia) == "PT"
                    hor_trabaj += 6
            elif turno == "FT":
                if hor_trabaj + 6 <= hor_contra:
                    turnos(empleado("nombre"))(dia) == "FT"
                    hor_trabaj += 6
    return turnos 


def escribir_archivo(kamila_urrego, empleados, turnos):
    with open(kamila_urrego, 'w') as archivo:

        encabezado = "nombre; turnos; horas trabaja; horas contra\n"
        archivo.write(encabezado)
        
        for empleado in empleados:
            nombre = empleado("nombre")
            turnos_asignados = "".join(turnos.get(nombre, (" ") * 31))
            horas_trabajadas = empleado("horas_trabajadas")
            horas_contratadas = empleado ("horas_contratadas")
            linea = f"{nombre};{turnos_asignados};{horas_trabajadas};{horas_contratadas}\n"
            archivo.write(linea)

def main():
    datos = (leer_archivo('kamila_urrego.txt'))
    print(datos)
    
    usuarios= (lista_empleados('lista_strings'))
    print(usuarios)

    turnos = asignacion_turnos('empleado')
    print(turnos)

    escribir= escribir_archivo('kamila_urrego', 'empleados'and 'turnos')
    print(escribir)
   

if __name__ == '__main__':
    main()




















    








