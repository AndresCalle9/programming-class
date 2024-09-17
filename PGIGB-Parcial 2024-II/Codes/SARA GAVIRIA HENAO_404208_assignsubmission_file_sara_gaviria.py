import random 

def  leer_archivo(ruta):
    with open (ruta,"r",encoding="utf-8") as file:
        output= [i.strip() for i in file][1:]
    return output

def lista_empleados(info):
    diccionario = {}
    lista=[]
    for i in info:
        aux = i.split(";")
        diccionario = {
            "nombre" : aux[0],
            "horas_contratadas" : int(aux[33]),
            "horas_trabajadas" : int(aux[32])
        }
        lista.append(diccionario)
    return lista

def asignar_turnos(empleados):
    diccio = {}
    empleados_aux = []
    for empleado in empleados:
        diccio[empleado['nombre']] = ['' for _ in range(0,32)]
        empleados_aux.append(empleado["nombre"])
    turnos = ["C", "C", "C", "N", "N", "N", "PT", "FT"]  
    horas_turno = {"C": 12, "N": 12, "PT": 6, "FT": 6}  
    for dia in range(1,32):
        for turno in turnos:
            empleado_asignado = random.choice(empleados)
            horas_restantes = int(empleado_asignado['horas_contratadas']) - int(empleado_asignado['horas_trabajadas'])
            if horas_restantes >= horas_turno[turno]:
                diccio[empleado_asignado['nombre']][dia-1] = turno
                empleado_asignado['horas_trabajadas'] += horas_turno[turno]
    
    return diccio


   
# def escribir_archivo (ruta, lista_empleados, diccionario):

#     print(lista_empleados,diccionario)
#     # with open (ruta, "w", encoding="utf-8") as file:
#     #     file.write()
        


def main ():
    info = leer_archivo("sara_gaviria.txt")
    empleados = lista_empleados(info)
    #print(empleados)
    cuadro_turnos = asignar_turnos(empleados)
    print(cuadro_turnos)
    # escribir_archivo("test.txt",empleados,cuadro_turnos)


if __name__ == "__main__":
    main()