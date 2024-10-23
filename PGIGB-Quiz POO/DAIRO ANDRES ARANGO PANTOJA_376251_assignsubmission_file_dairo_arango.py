import random
class Archivo:
    def __init__(self,ruta):
        self.ruta = ruta
        self.info = []

    def leer(self):
        with open(self.ruta ,'r',encoding='utf-8')as file:
            self.info = [ i.strip() for i in file]
        
    def escribir(self,ruta,metodo,datos):
        with open(ruta,metodo,encoding='utf-8')as file:
            for i in datos:
                file.write(i)
            file.write('\n')

    def aleatorio(self,datos):
        cont = ''
        cont2 = 1
        while cont2 <= 20:
            for i in datos:
                carcater = random.choice(i)
                cont += carcater
                cont2 += 1
        return(cont)
    
class Strings:
    def __init__(self,texto):
        self.texto = texto

    def cadenas(self):
        cadena1 = ''
        cadena2 = ''
        cont2 = 1
        while cont2 <= 20:
            for i in self.texto:
                carcater = random.choice(i)
                cadena1 += carcater
                carcater = random.choice(i)
                cadena2 += carcater
            cont2 += 1
        return(cadena2,cadena1)
        

class Morse:
    def __init__(self,texto1):
        self.texto1 = texto1
    
    def traduccion(self,texto):
        aux1 = self.texto1(', ')
        for i in texto:
            aux = i.upper()
            for j in aux:
                x =self.buscar(self.texto1,j,0)
                y = self.texto1[2]
                return aux1   

            
    def buscar(self,dato,target,columna):
        idx = ''
        for dato in dato:   
            aux = dato.split(',')
            if aux[columna] == target: 
                idx = dato.index(dato)
        return idx
                
    
archivo = Archivo('Texto.txt')
archivo.leer()
print(archivo.info)
print('''


     ''')
archivo.escribir('Dairo.txt','a',archivo.info)
caracteres = archivo.aleatorio(archivo.info)
print(caracteres)
print('''
      
      


    ''')

strings = Strings(archivo.info)
x = strings.cadenas()
print(x)
archivo.escribir('resultados.txt','a',x)






print('''




    ''')

