def leer(ruta,target):
    with open(ruta, 'r', encoding='utf-8') as file:
        lista = [i.strip() for i in file if i.count(target)==0]
    return lista

def buscar(datos,target,columna):
    idx = ''
    for i in datos:
        aux = i.split(';')
        if aux[columna] == target:
            idx = aux.index(i)
    return idx
    
def main():
    archivo = leer('turnos_asignados.txt','Nombre')
    cont = 0
    tipos_turnos = ['C', 'C', 'C', 'N', 'N', 'N', 'PT', 'FT']
    for i in archivo:
        aux = i.split(';')
        print(aux[1])
        for i in tipos_turnos:
            opt = buscar(archivo,i,0)
            if opt != '':
                cont+=1

        
if __name__=='__main__':
    main()
