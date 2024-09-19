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
    dic={}
    list=[]
    for i in range(len(ark)):
        aux=ark[i].split(';')
        dic={'Nombre':[aux[0]],
            'h_contratadas':[aux[33]],
            'h_trabajadas':aux[32]}
        list.append(dic)
    return list


def asignar_turnos(lista):
    ark=leer(lista)
    l=[]
    for linea in range(len(ark)):
        aux=ark[linea].split(';')
        l.append(aux[0])

    dias=0

    for persona in l:
        add=0
                
        while dias<31:
            must=['C','C','C','N','N','N','PT','FT']
            turnos={'C':12,
                    'N':12,
                    'PT':6,
                    'FT':6}
            
            t=random.choice(must)
            trn=';'.join(t)
            add+=turnos[t]
            dias+=1
    
    return persona, trn, add, aux,l

def main():
    print('--- ---')
    ruta='mariana_restrepo.txt'
    info=leer(ruta)
    print(info)
    print('--- ---')
    print(lista_empleados(ruta))
    
    datos='Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contratadas'
    escribir(ruta,'w',[datos])
    empleado,turnos,total,aux,l=asignar_turnos(ruta)
    for persona in l:
        final=f'{empleado};{turnos};{total};{aux[33]}'
        escribir(ruta,'a',[final])

if __name__=='__main__':
    main()

