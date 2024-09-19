#Crear una funcion que lea el txt y entregue en consola una lista si se cumplen los 8 turnos diarios o no

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file if line.count('Nombre') != 1]
        return datos 

def verificar(datos):
    turnos = []
    turnos_necesarios = ['C'] + ['C'] + ['C'] + ['N'] + ['N'] + ['N'] + ['PT'] + ['FT']
    for dato in datos:
        turnos.append(datos[-1])
        if turnos == turnos_necesarios:
            return True 
        
def main():
    info = leer_archivo('paulina_restrepo.txt')
    turno = verificar(info)

if __name__== '__main__':
    main()
