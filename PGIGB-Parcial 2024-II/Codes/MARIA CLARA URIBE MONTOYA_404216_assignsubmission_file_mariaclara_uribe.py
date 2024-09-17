import random

def leer_archivo(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        output = [i.strip() for i in file][1:]
    return output 

def escribir_archivo(ruta,metodo,lista,info):
    with open(ruta,metodo,encoding='utf-8') as file:
        file.write(lista,info)


def lista_empleados(lista):
    out = []
    for linea in lista:
        datos = linea.split(";")       
        nombre = datos[0]  
        horas_trabajadas = int(datos[-2])  
        horas_contratadas = int(datos[-1]) 
        
        empleado = {
            "nombre": nombre,
            "horas_trabajadas": horas_trabajadas,
            "horas_contratadas": horas_contratadas
        }
        out.append(empleado)  
    return out


def asignar_turnos(lista_personas):
    turnos = ['C']*3 + ['N']*3 + ['PT']*1 + ['FT']*1
    horas = {'C': 12,
             'N': 12,
             'PT': 6,
             'FT': 6}
    dias = 31
    asignaciones = {}
    for persona in lista_personas:
        nombre = persona['nombre']
        asignaciones[nombre] = [''] * dias
    for dia in range(dias):
        turnos_dia = turnos[:] 
        random.shuffle(turnos_dia)   
        for turno in turnos_dia:
            empleado_asignado = False
            while not empleado_asignado:
                empleado = random.choice(lista_personas)  
                nombre = empleado['nombre']
                horas_trabajadas = 0
                for x in asignaciones[nombre]:
                    if x in horas:
                        horas_trabajadas += horas[x]         
                if horas_trabajadas + horas[turno] <= empleado['horas_contratadas']:
                    asignaciones[nombre][dia] = turno
                    empleado_asignado = True
                    
    return asignaciones


def main():
    info = leer_archivo('mariaclara_uribe.txt')
    lista = lista_empleados(info)
    final = asignar_turnos(lista)
    print(final)






if __name__ == '__main__':
    main()





