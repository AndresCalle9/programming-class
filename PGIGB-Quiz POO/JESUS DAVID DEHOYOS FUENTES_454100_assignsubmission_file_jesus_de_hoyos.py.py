import random

class Archivos:
    def __init__(self, ruta):
        self.ruta = ruta
        self.info = []
        self.headers = ''
    
    def leer(self):
        with open(self.ruta,'r', encoding='utf-8') as file:
            self.info = [i.strip() for i in file]

    def write(self, method, ruta_aux='', datos = []):
        if ruta_aux == '':
            ruta_aux = self.ruta
        if len(datos) == 0:
            datos = self.info
        with open(ruta_aux,method,encoding='utf-8') as file:
            if method == 'w' and self.headers != '':
                file.write(self.headers + '\n')
            for line in datos:
                file.write(line)
    
    def random(self):
        for i in self.info:
            aux = i.split(',')
            texto = random.choice(aux)

        return texto

            
class Strings:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.str = [str1, str2]
 
    def discriminar(self):
        out1 = []
        out2 = []
        for i in self.str1:
            for j in self.str2:
                if i not in self.str2:
                    out1.append(i)
                if j not in self.str1:
                    out2.append(j)
        
        return out1, out2

    def crear_documento(self):
        reporte = Archivos('resultados.txt')
        reporte.write('w', '', ['Strings;Str1;Str2;Out1;Out2'])

        
class Morse:
    def __init__(self, documento):
        self.documento = documento
    
    def traduccion(self, texto):
        self.texto = texto
        texto_traducido = []
        while self.documento[0] == texto:
            texto_traducido.append(self.documento[1])

        return texto_traducido
    
    def escribir_morse(self):
        reporte2 = Archivos('resultados.txt')
        reporte2.write('a', '', ['Morse, texto traducido'])
        



Archivo1 = Archivos('Texto.txt')
leer = Archivo1.leer()
azar1 = Archivo1.random()
azar2 = Archivo1.random()
print(azar1)
print(azar2)
Proceso = Strings(azar1, azar2)
Disc = Proceso.discriminar()
print(Disc)
impr = Proceso.crear_documento()
Archivo2 = Archivos('Morse.txt')
leer2 = Archivo2.leer()
Proceso2 = Morse(leer2)
tradu = Proceso2.traduccion(leer)
escri = Proceso2.escribir_morse()

