import random

class Archivo():
    def __init__(self,ruta):
        self.ruta = ruta
        self.info = []

    def leer(self):
        with open(self.ruta, 'r', encoding='utf-8') as file:
            self.info = [i.strip() for i in file]
        return self.info
        
    def escribir(self,metodo,datos):
        with open(self.ruta,metodo,encoding='utf-8') as file:
            for line in datos:
                file.write(line + '\n')

    def randomm(self):
        cont = 0 
        cadena_texto = []
        while cont <= 5:
            for i in self.info:
                aux = i.split(' ')
                for i in range(len(aux)):
                    cadena = random.choice(aux)
                    cadena_texto.append(cadena)
                    cont += 1
                    break                    
        return ' '.join(cadena_texto)


class Hola():
    def __init__(self):
        self = self 

    def comparar_cadenas(self, str1, str2):
        out1 = ''.join([i for i in str1 if i not in str2])
        out2 = ''.join([i for i in str2 if i not in str1])
        return out1, out2



def main():
    ruta = 'texto.txt'
    mose = Archivo(ruta) 
    mose.leer()
    a = mose.randomm()
    b = mose.randomm()
    letras = Hola()
    final1= letras.comparar_cadenas(a,b)
    final1 = list(final1)
    ruta2 = 'mariaclaraa_uribe.txt' 
    otro = Archivo(ruta2)
    otro.escribir('a',final1)
    print(final1)




if __name__ == '__main__':
    main()








