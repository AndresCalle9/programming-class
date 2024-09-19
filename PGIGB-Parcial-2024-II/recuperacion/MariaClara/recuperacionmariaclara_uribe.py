def leer(ruta):
    with open(ruta,'r',encoding='utf-8') as file:
        output = [i.strip() for i in file][1:]
    return output
   

def validacion():
    pass
   



def main():
    info = leer('mariaclara_uribe2.txt')
    print(info)

    
        


if __name__ == '__main__':
    main()