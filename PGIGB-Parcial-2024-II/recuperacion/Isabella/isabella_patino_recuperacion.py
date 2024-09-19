#funcion que diga que dias tienen 8 turnos y que dias no tienen 8 turnos
def leer(ruta):
    try:
        with open(ruta,'r', encoding='utf-8') as file:
            output=[i.strip() for i in file]    
        return output
    except FileNotFoundError:
        return[]
    
def verificar():
    datos=leer('isabella_patino.txt')
    output_cumplio=[]
    output_no_complio=[]
    for i in range (1,len(datos)):
        aux= datos[i].split(';') 
        dia=1
        if aux[dia]==8:
            output_cumplio.append(dia)
        else:
            output_no_complio.append(dia)
    
def main():
    verifica=verificar()
    print(verifica)

if __name__=='__main__':
    main()