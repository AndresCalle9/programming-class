

class Archivo():
    def __init__(self,leer, write):
        with open('archivo.txt', 'w'):
            write('Todo se pudrio, auxilio')
        with open('archivo.txt', 'r'):
            print(leer.readlines())




class Esperanza():
    def __init__(self, ecuacion, numero,numero2):
        numero = 0
        numero2 = 1
        contador = 0
        list =[0, 1 ]
        a = 1
        self.ecuacion = ecuacion
        while contador <= 100:
            numerito = list.index(0)
            numero2 = list.index(numero+a)
            ecuacion = numerito + numero2
            a = ecuacion
            contador +=1
            list.append(a)
            print(list)
            if contador >= 1:
                numeron = numero2 - numerito
                numero3 = list.index(contador)
                if numero3 > 2:
                    numero3 = contador
                suma = numeron + numero3
                list.append(suma)
                numero +=1
        if ValueError:
            print('Eso es todo amigos')

Esperanza(sum, 0,1)