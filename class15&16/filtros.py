def read(ruta):
    with open (ruta,'r', encoding='utf-8') as f:
        output = [i.strip() for i in f]
    return output

#Función que convierte una lista de strings en una lista de diccionarios
def to_dict(lista):
    output = []
    headers = lista[0].split(',')
    for i in range(1,len(lista)):
        aux = lista[i].split(',')
        dicc = {}
        for j in range(len(headers)):
            dicc[headers[j]] = aux[j]
        output.append(dicc)
    return output

# filtrar de una lista de strings separados por comas
def filtrar_num(lista, columna, valor):
    output = []
    for i in range(1,len(lista)):
        aux = lista[i].split(',')
        if int(aux[columna]) >= valor:
            output.append(lista[i])
    return output

def filtrar_str(lista, columna, valor):
    output = []
    for i in range(1,len(lista)):
        aux = lista[i].split(',')
        if aux[columna] == valor:
            output.append(lista[i])
    return output

def main():
    datos = read('datos.txt')
    datos_dict = to_dict(datos)

    # encontrar los mayores de 30 años
    mayores_30 = [i for i in datos_dict if int(i['age']) > 40 and i['language'] == 'python']
    print(mayores_30)

    mayores_50_str = filtrar_num(datos,1,50)
    print(mayores_50_str)
    trabajan_ces = filtrar_str(datos,2,'CES')
    print(trabajan_ces)
    sum = 0
    for i in trabajan_ces:
        aux = i.split(',')
        sum += int(aux[1])
    print(sum/len(trabajan_ces))
    

if __name__ == "__main__":
    main()