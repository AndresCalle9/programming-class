import random
class Archivo: 
    def __init__(self,ruta):
        self.ruta=ruta
        self.headers=''
        self.info=[]

    def read(self):
        with open(self.ruta, 'r', encoding='utf-8') as file:
            self.info=[i.strip() for i in file]

    
    def write(self, metodo, ruta_aux, datos=[]):
        if ruta_aux=='':
            ruta_aux=self.ruta
        if len(datos)==0:
            datos=self.info
        with open(ruta_aux, metodo, encoding='utf-8') as file:
            if metodo=='w' and self.headers!='':
                file.write(self.headers + '\n')
            
            for line in file:
                file.write(line + '\n')

    def aleatorio(self):
        caracters=[i.split(' ') for i in self.info]
        caracters_random=random.choice(caracters)

        return caracters_random




class Strings:
    def __init__(self, str1, str2):
        self.str1=str1
        self.str2=str2

    def salida(self):
        self.out_1=[]
        self.out_2=[]
        for i in str1.info:
            if i not in str2.info:
                self.out_1.append(i)
        for j in str2.info:
            if j not in str1.info:
                self.out_2.append(j)

        return self.out_1,self.out_2
    
    def generar_reporte(self):
        reporte=Archivo('resultados.txt')
        reporte.write('w','', f'{self.str1};{self.str2}; {self.out_1},{self.out_2}')

class Morse:
    def __init__(self,text):
        self.text=text

    def traduccion(self):
        pass





archivo=Archivo('Texto.txt')
archivo.read()
str1=archivo.aleatorio()
str2=archivo.aleatorio()
strings=Strings(str1,str2)
strings.salida()
strings.generar_reporte()
morse=Archivo('Morse.txt')
usar_morse=Morse(morse)













