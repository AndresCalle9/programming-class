def check(way, lista):
    result = False
    for i in range(len(lista)):
        if way[i] == lista[i]:
            result = True
        else:
            result = False
            break
    return result

def main():
    way = ['A','I','D','Z']
    lista = []
    menu = '''
        Como te gustaria avanzar:

        A) Adelante
        I) Izquierda
        D) Derecha
        Z) Atras
    '''
    while True:
        print(menu)
        print(way,lista)
        opt = input('Ingresa una opcion: ')
        lista.append(opt)
        flag = check(way, lista)
        if flag:
            print('Vas por el camino correcto')
            if len(lista) == len(way):
                print('Felicidades, has llegado al final del camino')
                break
        else:
            print('Vas por el camino incorrecto')
            while True:
                if len(lista)>0:
                    flag_2 = check(way, lista)
                    if flag_2 == True: #flag_2
                        print('Volviste al camino correcto')
                        break
                    else:
                        print('Desea regresar o seguir: 1) regresar, 2) Seguir')
                        opt_two = input('Ingresa una opcion: ')
                        if opt_two == '1':
                            lista.pop()
                            print(lista)
                        else:
                            break
                else:
                    print('Volviste al inicio')
                    break
            
   

if __name__ == '__main__':
    main()
