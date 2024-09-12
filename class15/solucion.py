def read(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]
    return datos

def write(ruta,metodo,datos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')

# TASK: Asignar pesos a las 6 notas

def asignar_pesos(info):

    porcentaje = int(info[1].split(',')[len(info[0].split(','))-1]) / (len(info[0].split(',')) - 1)
    for i in range(0,(len(info[0].split(','))-1)):
        aux = info[1].split(',')
        aux[i] = str(porcentaje)
        info[1] = ",".join(aux)

    return info

# TASK: Encuentre la nota (nota*peso) de cada usuario y actualice totales.txt
def actualizar_notas(pesos, notas):
    totales = read('totales.txt')
    for fila in range(1,len(notas)):
        aux = notas[fila].split(',')
        for col in range(1,len(aux)):
            valor = float(aux[col])*(float(pesos[1].split(',')[col-1])/100)
            temp = totales[fila].split(',')
            temp[col] = str(valor)
            totales[fila] = ",".join(temp)
    
    return totales

# TASK: función que cree un archivo llamado final.txt con los nombres delos estudiantes y sus notas finales

def ponderar_notas(notas):
    final = ['Nombre del Estudiante, Nota final']
    for fila in range(1,len(notas)):
        aux = notas[fila].split(',')
        suma = 0
        for col in range(1,len(aux)):
            suma += float(aux[col])
        final.append(aux[0]+','+str(suma))
    return final

def main():
    pesos = read('pesos.txt') #se borra si se usa la version recursiva
    pesos_actualizados = asignar_pesos(pesos) #no lleva parametro si se usa la versión recursiva
    print(pesos_actualizados)
    write('pesos.txt','w',pesos_actualizados)
    notas = read('notas.txt')
    notas_actualizadas = actualizar_notas(pesos_actualizados,notas)
    print(notas_actualizadas)
    write('totales.txt','w',notas_actualizadas)
    notas_finales = ponderar_notas(notas_actualizadas)
    print(notas_finales)
    write('final.txt','w',notas_finales)


if __name__ == '__main__':
    main()