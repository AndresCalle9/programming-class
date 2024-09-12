def read(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]
    return datos

def write(ruta,metodo,datos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')

# TASK: Asignar pesos a las 6 notas

# def asignar_pesos(index = 0):
#     info = read('pesos.txt')

#     if index == (len(info[0].split(',')) - 1):
#         return read('pesos.txt')
    
#     porcentaje = int(info[1].split(',')[len(info[0].split(','))-1]) / (len(info[0].split(',')) - 1)
    
#     aux = info[1].split(',')
#     aux[index] = str(porcentaje)
#     info[1] = ",".join(aux)
#     write('pesos.txt','w',info)

#     return asignar_pesos(index + 1) #Recursividad

def asignar_pesos(info):

    porcentaje = int(info[1].split(',')[len(info[0].split(','))-1]) / (len(info[0].split(',')) - 1)
    for i in range(0,6):
        aux = info[1].split(',')
        aux[i] = str(porcentaje)
        info[1] = ",".join(aux)

    return info

# Encuentre la nota (nota*peso) de cada usuario y actualice totales.txt
def actualizar_notas(pesos, notas):
    totales = read('totales.txt')
    for idx in range(1,len(notas)):
        aux = notas[idx].split(',')
        for j in range(1,len(aux)):
            valor = float(aux[j])*(float(pesos[1].split(',')[j-1])/100)
            temp = totales[idx].split(',')
            temp[j] = str(valor)
            totales[idx] = ",".join(temp)
    
    return totales

def main():
    pesos = read('pesos.txt') #se borra si se usa la version recursiva
    pesos_actualizados = asignar_pesos(pesos) #no lleva parametro si se usa la versión recursiva
    print(pesos_actualizados)
    write('pesos.txt','w',pesos_actualizados)
    notas = read('notas.txt')
    notas_actualizadas = actualizar_notas(pesos_actualizados,notas)
    print(notas_actualizadas)
    write('totales.txt','w',notas_actualizadas)

if __name__ == '__main__':
    main()