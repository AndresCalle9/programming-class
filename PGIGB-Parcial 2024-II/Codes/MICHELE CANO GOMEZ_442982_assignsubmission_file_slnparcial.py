import random

def leer_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as file:
        lineas = [line.strip() for line in file]
        lineax = lineas[1:]
    return lineax

def write(ruta, metodo, data):
    with open(ruta, metodo, encoding="utf-8") as file:
        for i in data:
            file.write(i)

def dic_empleados(lineax):
    lista = []
    for i in lineax:
        aux = i.split(";")
        dic ={"Nombre": aux[0],
              "Trabajadas": aux[32],
              "Contratadas": aux[33]}
        lista.append(dic)
    return lista, dic

def lista_empleados(lineax):
    empleados = []
    for i in lineax:
        aux = i.split(";")
        empleados.append(aux[0])
    return empleados

def cuadro_turnos(empleados, lista, dic): 
    C1 = "C1" 
    C2 = "C2"
    C3 = "C3"
    N1 = "N1"
    N2 = "N2"
    N3 = "N3"
    FT = "FT"
    PT = "PT"

    C1 = 12
    C2 = 12
    C3 = 12
    N1 = 12
    N2 = 12
    N3 = 12
    FT= 6
    PT= 6

    dicc = {}
    turnos = ['C1','C2','C3','N1','N2','N3','FT','PT']

    for empleado in empleados:
        dicc[empleado] = [' ' for i in range(0,32)]

    cont = 0
    while cont < 31:
        for turno in turnos:
            aux = random.choice(empleados)
            print(cont,turno,aux)
        for i in dic:
            if dic["Nombre"] == [empleado]:
                if int(dic["Contratadas"]) >= [turno] and int(dic["Trabajadas"]) <= [turno]:
                    dicc[aux][cont] = turno #Para poder hacer esto hay que verificar las horas de cada empleado
        cont += 1


#def escribir_archivo():
#    write("C:/Users/USUARIO/Documents/Miche/tallerpy/Parcial2/test.txt", "w", ["Nombre del empleado, Turnos asignados", "Horas trabajadas para cada día del mes", "Horas contratadas"])
#    write("C:/Users/USUARIO/Documents/Miche/tallerpy/Parcial2/test.txt", "a",)



def main():
    lineax = leer_archivo("C:/Users/USUARIO/Documents/Miche/tallerpy/Parcial2/asly_amado.txt")
    dic, lista = dic_empleados(lineax)
    empleados = lista_empleados(lineax)
    #print(dic)
    #print(empleados)
    turnos_asg = cuadro_turnos(empleados, dic, lista)
    print(turnos_asg)

if __name__ == "__main__":
    main()
