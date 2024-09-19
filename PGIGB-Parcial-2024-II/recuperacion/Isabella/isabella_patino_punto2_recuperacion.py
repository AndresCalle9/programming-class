import random
def leer(ruta):
    try:
        with open(ruta,'r', encoding='utf-8') as file:
            output=[i.strip() for i in file]    
        return output
    except FileNotFoundError:
        return[]

def write(ruta,metodo,datos):
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
    for i in range(1,len(datos)): 
        aux = datos[i].split(';') 
        dicc = {
            'nombre':str(aux[0]),
            'horas trabajadas': int(aux[32]),
            'horas contratadas':int(aux[33])
        }
        output.append(dicc)
    return output

def asignar_turnos(datos):
   
    trabajadores=[]
    for i in range(1,len(datos)):
        aux=datos[i].split(';')
        trabajadores.append(aux[0])
        dias=1
    while dias<32:
        contador=0
       
        while contador < 8:
            
            turnos=['C','C','C','N','N','N','PT','PT']
            for i in range(0,len(turnos)):
                
                trabajador=random.choice(trabajadores)
                turno=random.choice(turnos)
                
                
                output=[]
                dicc={
                    'nombre': trabajador,
                    'turno': turno
                        }
                output.append(dicc)
            return output
        contador +=1
        print(f'contador : {contador}')
        
    dias +=1
    print(f'dias: {dias}')
    return output
            



def main():
    info=leer_archivo()
    print(info)

    datos=leer('isabella_patino.txt')
    diccionarios=crear_diccionario(datos)
    print(diccionarios)

    asignar=asignar_turnos(datos)
    print(asignar)

if __name__=='__main__':
    main()