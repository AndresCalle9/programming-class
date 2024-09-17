import random
def leer(ruta,target):
    with open(ruta,'r',encoding='utf-8')as file:
        lista = [i.strip() for i in file if i.count(target)==0]
    return lista 

def escribrir(ruta,metodo,datos):
    with open(ruta,metodo,encoding='utf-8')as file:
        file.write(datos + '\n')

def lista_de_empleados(info):
    for i in info:
        aux=i.split(';')
        nombre = aux[0]
        horas = aux[33]
        traba = aux[32]
        diccio={
            'Nombre':nombre,
            'Horas_contadas':horas,
            'Horas_trabajadas' :traba
                    }
        print(diccio)
    return diccio

def asignar_turnos(archivo):
    lista = ['C','N','PT','FT']
    listaaux = []
    while len(listaaux) <= 31:
        eleccion = random.choice(lista)
        listaaux.append(eleccion)
    print(listaaux)
    listaname = []
    for i in archivo:
        aux=i.split(';')
        nombre = aux[0]
        listaname.append(nombre)
        diccionario = {
            nombre : listaaux
            }
        print(diccionario)

def main():
    archivo = leer('test.txt','Nombre')
    lista_de_empleados(archivo)
    asignar_turnos(archivo)


    
if __name__=='__main__':
    main()

