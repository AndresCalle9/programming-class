def leer_archivo(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        datos=[line.strip() for line in file][1:]
    return datos



def lista_data():
   empleados=[]
   datos=leer_archivo('asly_amado.txt')
   for linea in datos:
    linea = linea.strip().split(';')
    for i in linea:
        nombre = i[0:].split(';')
        horas_trabajadas = i[32:].strip(';')
        horas_contratadas = i[33:].strip(';')
        empleado = {
            'nombre': nombre,
            'horas_trabajadass': horas_contratadas,
            'horas_contratadas': horas_trabajadas
            }
    empleados.append(empleado)
            
    return empleados
        
        
def main():
    info=leer_archivo('asly_amado.txt')
    print(info)
    empleadoss=lista_data()
    print(empleadoss)
    
if __name__=='__main__':
    main()