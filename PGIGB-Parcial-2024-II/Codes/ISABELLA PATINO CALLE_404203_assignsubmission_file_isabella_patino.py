import random
def leer(ruta):
    try:
        with open(ruta,'r', encoding='utf-8') as file:
            output=[i.strip() for i in file]
            
        return output
    except FileNotFoundError:
        return[]

def escribir(ruta,metodo,datos):
    with open(ruta,metodo,encoding='utf-8') as file:
        #for i in datos:
            file.write(datos+'\n')

def leer_archivo():
    datos=leer('isabella_patino.txt')
    output = []
    
    for i in range(1,len(datos)): 
        aux = datos[i].split(';') 
        output.append(aux)
    return output



def crear_diccionario(datos):
    output = []
    #headers = datos[0].split(';')
    for i in range(1,len(datos)): 
        aux = datos[i].split(';') 
        dicc = {
            'nombre':aux[0],
            'horas trabajadas': aux[32],
            'horas contratadas':aux[33]
        }
        # for j in range(len(headers)):
            # dicc[headers[j]] = aux[j]
        output.append(dicc)
    return output


def asignar_turnos(datos):
    contador_dias=1
    lista=leer('isabella_patino.txt')
    trabajadores=[]
    for i in range(1,len(datos)):
        aux=datos[i].split(';')
        
        trabajadores.append(aux[0])
    while contador_dias<32:
        output = []
        for i in range(1,len(datos)): 
            aux1 = datos[i].split(';')
        #contadores
        C=0
        N=0
        PT=0
        FT=0
        horas_trabajadas=aux1[32]
        horas_contratadas=aux1[33]
        repetidos=[]
        while C<3 and N<3 and PT==1 and FT==1:
            if C<3:
                horas_C=12
                trabajador=random.choice(trabajadores)
                repetidos.append(trabajador)
                if trabajador not in trabajadores :
                    if aux1[0]==trabajador and horas_C<horas_trabajadas and horas_C<horas_contratadas:
                        aux1[contador_dias]=C
                    C+=1
                    horas_trabajadas+=horas_C
            if N<3:
                horas_N=12
                trabajador=random.choice(trabajadores)
                repetidos.append(trabajador)
                if trabajador not in trabajadores:
                    if aux1[0]==trabajador and horas_N<horas_trabajadas and horas_N<horas_contratadas:
                        aux1[contador_dias]=N
                    N+=1
                    horas_trabajadas+=horas_N
            if PT<1:
                horas_PT=6
                trabajador=random.choice(trabajadores)
                repetidos.append(trabajador)
                if trabajador not in trabajadores:
                    if aux1[0]==trabajador and horas_PT<horas_trabajadas and horas_PT<horas_contratadas:
                        aux1[contador_dias]=PT
                    PT+=1
                    horas_trabajadas+=horas_PT
            if FT <1:
                horas_FT: 6
                trabajador=random.choice(trabajadores)
                repetidos.append(trabajador)
                if trabajador not in trabajadores:
                    if aux1[0]==trabajador and horas_FT<horas_trabajadas and horas_FT<horas_contratadas:
                        aux1[contador_dias]=FT
                    FT+=1
                    horas_trabajadas+=horas_FT

        contador_dias +=1
        diccionario={
            aux1[0]:[range(aux[1],aux[32])]
         }

        output.append(diccionario)

    return output
        


def main():
    print('---punto1-----')
    list=leer_archivo()
    print(list)
    
    print('---punto2---')
    lista=leer('isabella_patino.txt')
    dicc=crear_diccionario(lista)
    print(dicc)

    print('---punto 3---')
    lista=leer('isabella_patino.txt')
    dict=asignar_turnos(lista)
    print(dict)
    escribir('patino_isabella.txt','w',['Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;horas trabajadas;horas contraradas'])
    escribir('patino_isabella.txt','a',dict)
if __name__=='__main__':
    main()