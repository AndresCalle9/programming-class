import random

def leer_archivo(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        output = [i.strip() for i in file][1:]
    return output 

def escribir_archivo(ruta,metodo,info):
    with open(ruta,metodo,encoding='utf-8') as file:
        file.write(f'{info}' + '\n')


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
    escribir_archivo('mariaclara_uribe2.txt','a','Nombre;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31')
    for i in final.items():
        escribir_archivo('mariaclara_uribe2.txt','a',list(i))
        


    



# Crear un archivo que valide que la solución del examen está bien


if __name__ == '__main__':
    main()





