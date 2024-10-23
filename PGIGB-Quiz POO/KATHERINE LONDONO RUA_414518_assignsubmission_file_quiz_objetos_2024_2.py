# Seccion1:
import random
class Archivos:
    def __init__(self, ruta):
        self.ruta= ruta
        #self.encabezado=''
        self.info=[]

    def leer(self):
        with open(self.ruta, 'r', encoding='utf-8') as file:
            self.info=[linea.strip() for linea in file]
            #self.encabezado=self.info[0]
            #self.info.pop(0)
    
    def escribir(self, ruta_aux, metodo, mensaje):
        if ruta_aux=='':
            ruta_aux= self.ruta
        # if len(mensajes)==0:
        #     mensajes= self.info
        
        with open(self.ruta, metodo, encoding='utf-8') as file:
            if metodo=='w' and self.encabezado !='':
                file.write(self.encabezado + '\n')
            file.write(mensaje + '\n')

    def random(self):
        for i in self.info:
            aux= i.split(' ')
            cadeena_aleatoria= random.choice(aux)
        return cadeena_aleatoria

# Seccion 2
class String:
    def __init__(self):
        self.lista_cadena1=[]
        self.lista_cadena2=[]

    def cadenas_de_texto(self, str1, str2):
        for i in str1:
            if i not in str2:
                self.lista_cadena1.append(i)
        for j in str2:
            if j not in str1:
                self.lista_cadena2.append(j)

        out1=''
        out2=''
        for i in self.lista_cadena1:
            out1 +=i
        for j in self.lista_cadena2:
            out2+=j

        return out1, out2

#Seccion3
class Morse:   
    def __init__(self):
        self.informacio_morse=[]

    def traduccion(self, ruta):
        archivo= Archivos(ruta)
        archivo.leer()
        for i in archivo.info:
            print(i)


archivo1= Archivos('Texto.txt')
archivo1.leer()
ducpla_cadena=[]
cont=0
while cont < 2:
    random_cadena= archivo1.random()
    ducpla_cadena.append(random_cadena)
    cont +=1

print(ducpla_cadena)
str1=ducpla_cadena[0]
str2=ducpla_cadena[1]
string= String()
out1, out2= string.cadenas_de_texto(str1, str2)
print(out1)
print(out2)
linea= f'Strings;{str1},{str2},{out1},{out2}'
print(linea)
ruta_escribir='resultados.txt'
archivo_escribir= Archivos(ruta_escribir)
archivo_escribir.escribir(ruta_escribir,'a',linea)

morse=Morse()
morse.traduccion(ruta_escribir)


