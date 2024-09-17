import random

def read(ruta):
    with open(ruta,'r',encoding='UTF-8') as file:
        output = [i.strip() for i in file]
    output.pop(0)
    return output

def list_dicc(info):
    output =[]
    for i in info:
        aux = i.split(';')
        output.append({
            'nombre': aux[0],
            'horas_trabajadas': int(aux[32]),
            'horas_contratadas' : int(aux[33])
        })
    return output

def cuadro_turnos(usuarios):
    output ={empleado['nombre']:[""]*31 for empleado in usuarios}
    turnos_dicc ={
        'C':12,
        'N':12,
        'PT':6,
        'FT':6
    }
    for dia in range(31):
        turnos = ['C','C','C','N','N','N','PT','FT']
        for turno in turnos:
            asignado = False
            intentos = 0
            while not asignado and intentos < len(usuarios):
                elegido = random.choice(usuarios)
                horas_trabajadas = elegido['horas_trabajadas']
                if horas_trabajadas + turnos_dicc[turno] < elegido['horas_contratadas'] and output[elegido['nombre']][dia] == '':
                    output[elegido['nombre']][dia] = turno
                    elegido['horas_trabajadas'] += turnos_dicc[turno] 
                    asignado = True
                intentos += 1
                
    for key in output.keys():
        for empleado in usuarios:
            if key == empleado['nombre']:
                output[key].append(str(empleado['horas_trabajadas']))
                output[key].append(str(empleado['horas_contratadas']))
    return output

def write(ruta,metodo,datos):
    with open(ruta, metodo, encoding='UTF-8') as file :
        for i in datos:
            file.write(i)
        file.write('\n')

def main():
    datos = read('./class17/CT.txt')
    usuarios = list_dicc(datos)
    turnos = cuadro_turnos(usuarios)
    for usuario in usuarios:
       write('sln.txt','a',';'.join([usuario['nombre']]+turnos[usuario['nombre']]))
    
if __name__ == '__main__':
    main()