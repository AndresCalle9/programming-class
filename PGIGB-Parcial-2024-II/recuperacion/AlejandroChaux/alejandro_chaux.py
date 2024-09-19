# import random

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as file:
        info = [linea.strip() for linea in file]
    return info

def lista_empleados(datos):
    empleados = {}
    for i in range(1, len(datos)):
        linea = datos[i].split(";")
        nombres = linea[0]
        horas_vacias = linea[1:31]
        horas_trabajadas = linea[32]
        horas_contratadas = linea[33]

        if nombres not in empleados:
            empleados[nombres] = {
                "horas_vacias": horas_vacias,
                "horas_trabajadas": horas_trabajadas,
                "horas_contratadas": horas_contratadas
            }

    return empleados

# def asignar_notas(empleados):

#     turnos = {"C":12,"C":12,"C":12,"N":12,"N":12,"N":12,"PT":6,"FT":6}

#     for nombres in empleados:
#             for i in empleados[nombres]:
#                 for horas_vacias in nombres[i]:
#                     linea = horas_vacias[].split(";")
#                     for linea in linea:
#                         cuadro_turnos = horas_vacias.append(random.choice(turnos))
#     return cuadro_turnos

def main():
    info = leer_archivo("./alejandro_chaux.txt")
    empleados = lista_empleados(info)
    print(empleados)

    # cuadro_turnos = asignar_notas(empleados)
    # print(cuadro_turnos)




if __name__ == "__main__":
    main()