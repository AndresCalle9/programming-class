import random

tildes={'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
class Archivo:
    def __init__(self,ruta):
        self.ruta=ruta
        self.info=[]
        self.cadenas_caracteres=[]

    def leer(self,ruta_aux='',flag=False):
        if ruta_aux=='':
            ruta_aux=self.ruta
        with open(ruta_aux,'r', encoding='utf-8') as file:
            self.info=[i.strip() for i in file]
            if flag==True:
                for elem in self.info[0].split(','):
                    self.cadenas_caracteres.append(elem.lower())
            
    
    def escribir(self,metodo,datos,rut=''):
        if rut=='':
            rut=self.ruta
        with open(rut,metodo, encoding='utf-8') as file:
            for i in datos:
                file.write(i+'\n')
    
    def random(self):
        choice=random.choice(self.cadenas_caracteres)
        self.cadenas_caracteres.remove(choice)
        return choice
    
class Strings:
    def retornar_strings(self,str_uno,str_dos):
        out_uno=''
        out_dos=''
        for caract in str_uno:
            if not caract==' ':
                if caract not in out_uno:
                    if caract not in str_dos:
                        out_uno+=caract

        for caracter in str_dos:
            if not caracter=='':
                if caracter not in out_dos:
                    if caracter not in str_uno:
                        out_dos+=caracter
        
        return out_uno,out_dos

class Morse:
    def __init__(self,texto):
        self.texto=texto

    def traduccion_morse(self,traduccion):
        diccionario={}
        for line in traduccion:
            aux=line.split(',')
            diccionario[aux[0]]=aux[1]

        
        
        
    
archivo=Archivo('Texto.txt')
archivo.leer(flag=True)
prueba=Strings()
srt_uno=archivo.random()
srt_dos=archivo.random()
out_puts_uno,output_dos=prueba.retornar_strings(srt_uno,srt_dos)
print('1',out_puts_uno)
print('2',output_dos)
string_final=f'Strings;{srt_uno};{srt_dos};{out_puts_uno};{output_dos}'
lista=[string_final]
print(string_final)
archivo.escribir('w',lista,'resultado.txt')

archivo_morse=Archivo('Morse.txt')
archivo_morse.leer(flag=False)
morse=Morse(archivo.info[0])
morse.traduccion_morse(archivo_morse.info)

    