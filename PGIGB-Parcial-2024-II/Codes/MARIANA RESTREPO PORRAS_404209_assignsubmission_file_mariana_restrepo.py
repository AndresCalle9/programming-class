import random

def leer(ruta):
    lista=[]
    with open(ruta,'r',encoding='utf-8') as file:
        for i in file:
            lista.append(i.strip())
        lista.pop(0)
    return lista

def escribir(ruta,metodo,datos):
    with open(ruta,metodo,encoding='utf-8')as file:
        for dato in datos:
            file.write(dato+'\n')
         


def lista_empleados(ruta):
    ark=leer(ruta)
    output = []
    for i in range(len(ark)):
        aux = ark[0].split(';')
        dicc = {}
        for col in range(len(ark)):
            dicc[ark[i]] = aux[col]
            output.append(dicc)
    return output



def asignar_turnos(lista):
    ark=leer(lista)
    l=[]
    for linea in range(len(ark)):
        aux=ark[linea].split(';')
        l.append(aux[0])
    empleado=random.choice(l)
    horas=0
    turnos=['c','c','c','n','n','n','pt','ft']
    trabajara=random.choice(turnos)
    if trabajara=='c':
        horas+=12
    if trabajara=='n':
        horas+=12
    if trabajara=='pt':
        horas+=6
    if trabajara=='ft':
        horas+=6
    return f'{empleado};{horas}'




def main():
    input('Enter para leer el archivo.')
    ruta='test.txt'
    new_ruta='mariana_restrepo.txt'
    info=leer(ruta)
    print(info)
    lista_empleados(ruta)
    datos='Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contratadas'
    escribir(new_ruta,'w',[datos])
    for linea in range(len(info)):
        aux=info[linea].split(';')
        nombre=aux[0]
        x=[nombre,asignar_turnos(ruta)]
        escribir(new_ruta,'a',x)

if __name__=='__main__':
    main()