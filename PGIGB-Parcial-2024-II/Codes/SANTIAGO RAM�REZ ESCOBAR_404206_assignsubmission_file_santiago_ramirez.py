import random

def leer_archivo():
    with open('santiago_ramirez.txt', 'r', encoding = 'utf-8') as archivo:
        archivo.readline()

def lista_empleados(nombre, ht, hc):
    nombre = {}
    ht = {}
    hc = {}
    lista = [nombre, ht, hc]
    with open(lista, 'r') as file:
        file.write(lista)

def asignar_turnos():
    '''
    3 corridos (c) / 12 horas
    3 Noches (n) / 12 horas
    1 post turno(pt) /6 horas
    1 fast track (ft) / 6 horas
    son 15 personas
    '''
    trabajando = 0
    c = 3
    n = 3
    pt = 1
    ft = 1
    persona = random.randint(1,16)
    while trabajando <= 8:
        print(f'persona{persona}\n')
        trabajando += 1
        return persona
    pedro =random.choice(c,n,pt,ft)
    if pedro == c:
        print(f'Trabajo{persona}')

def main():
    info = leer_archivo()
    empleados = lista_empleados(info)
    ayuda = empleados(asignar_turnos)
    print(ayuda)

    
    

if __name__ == '__main__':
    main()