import random
class Archivo:
    def __init__(self, ruta):
        self.ruta =  ruta
        self.datos = []
        
    def leer(self):
        with open(ruta, 'r', encoding='utf-8') as file:
            salida = [i.stip() for i in file]
    
    def escribir(self, metodo, datos, cabecera = ''):
        if cabecera != '':
            cabecera == data1
        with open(self, self.ruta, metodo) as file:
            file.write(data1 + '\n')
            file.write(datos + '\n')


class Esperanza:
    def __init__(self, datos):
        self.datos =  datos
        self.fibo = []
        # self.armstrong = []
        # self.noarmstrong = []
    
    def fibonacci(self):
        lista = [0,1,1]
        for i in lista:
            i = lista[-1] + lista[-2]
            lista.append(i)
            if len(lista) > 100:
                print(lista)
                self.fibo.append(lista)
                break
    
    def armstrong(self):
        listaarmstron = []
        listanoarmstron = []
        for i in self.datos:
            #print(i)
            listaaux2 = []
            for j in str(i):
                a = int(j)
                b = a**3
                listaaux2.append(b)
            suma = 0
            for k in listaaux2:
                suma += k
            if suma == i:
                listaarmstron.append(i)
            else:
                listanoarmstron.append(i)
    
        #return listaarmstron, listanoarmstron

        print(listanoarmstron)
        print(listaarmstron)

def main():
    lista = []
    lista2 = range(0, 1000)
    for i in lista2:
        if i not in lista:
            i = random.choice(lista2)
            lista.append(i)
            if len(lista) > 3:
                lista.append(153)
                break
    
    #prueba2 = armstrong(lista)
    prueba = Esperanza(lista)
    prueba.fibonacci()
    prueba.armstrong()

if __name__ == '__main__':
    main()