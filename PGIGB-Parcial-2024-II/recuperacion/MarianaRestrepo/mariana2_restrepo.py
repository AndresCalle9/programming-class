def leer(ruta):
    with open (ruta,'r',encoding='utf-8') as file:
        l=[linea.strip() for linea in file]
    return l

def  verificar(ruta):
    pass    

def main():
    ruta='mariana_restrepo.txt'
    print(leer(ruta))

if __name__=='__main__':
    main()