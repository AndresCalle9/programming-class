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
              "Trabajadas": int(aux[32]),
              "Contratadas": int(aux[33])}
        lista.append(dic)
    return dic, lista

def lista_empleados(lineax):
    empleados = []
    for i in lineax:
        aux = i.split(";")
        empleados.append(aux[0])
    return empleados

def cuadro_turnos(empleados, dic, lista): 
    distrib = {}
    turnos = {"C1": 12, "C2": 12, "C3": 12, "N1": 12, "N2": 12, "N3": 12, "FT": 6, "PT": 6}

    dicc = {}
    for empleado in empleados:
        dicc[empleado] = [' ' for i in range(0,32)]

    cont = 0
    while cont < 31: #cont la columna del dia
        for turno in turnos:
            aux = random.choice(empleados)
            distrib[turno] = aux
            #print(cont, turno, aux)
        #print(distrib)
        for i in distrib.keys(): #i = C1, C2....
            for emplea in lista:
                if emplea['Nombre'] == distrib[i]:
                    if int(emplea["Trabajadas"]) <= turnos[i]:
                        dicc[distrib[i]][cont] = i
                        emplea['Trabajadas'] += turnos[i]                    
        cont += 1
    print(dicc)
    return turno, aux, distrib, dicc


def imprimir_tabla(distrib, empleados, turno, aux, dicc):
    auxx = []
    for i in aux:
        auxx.append(aux)

    write("michele_cano2.txt", "w", "Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas" + "\n" )
    for j in dicc:
        write("michele_cano2.txt", "a", j + "; " *32 +"\n")    


#un archivo adicional con una funcion que valide que la solucion del parcial esta bien, que llena el cuadro de turnos, una lista con los dias que tienen 8 puntos y otra con los que no los tienen

def main():
    lineax = leer_archivo("michele_cano.txt")
    dic, lista = dic_empleados(lineax)
    empleados = lista_empleados(lineax)
    #print(empleados)
    #print(dic)
    #print(empleados)
    turno, aux, distrib, dicc = cuadro_turnos(empleados, dic, lista)
    #print(turnos_asg)
    imprimir_tabla(distrib, empleados, turno, aux, dicc)
if __name__ == "__main__":
    main()
