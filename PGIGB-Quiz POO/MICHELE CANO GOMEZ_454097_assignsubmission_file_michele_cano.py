#¡PROFE YO APOYO AL DIM, CALÍFICAME CON AMOR, GRACIAS!

import random
#SECCIÓN 1
class Archivos():
    def __init__(self, ruta):
       self.ruta = ruta
       self.info = []
       self.cadenas = []

    def read(self):
       with open(self.ruta,'r', encoding='utf-8') as file:
        self.info = [i.split(" ") for i in file]
        return self.info

    def write(self, method, ruta_aux='', datos = []):
       if ruta_aux == '':
           ruta_aux = self.ruta
       if len(datos) == 0:
           datos = self.info
       with open(ruta_aux,method,encoding='utf-8') as file:
           for line in datos:
               file.write(line + '\n')

    def random(self):
        self.cadenas = []
        for i in self.info:
            self.cadenas.append(i)
        selec = random.choice(self.cadenas)
        return selec
    
texto = Archivos("Texto.txt")
textox = texto.read()
selec1 = texto.random()
selec2 = texto.random()
print(texto.info)

#SECCIÓN 2
class Strings():
    def __init__(self):
        pass

    def cadenax(self, str1, str2):
        control_str1 = []
        for i in str1:
            control_str1.append(i)
        for k in str2:
            for j in control_str1:
                if k == j:
                    control_str1.remove(j)
        control_str2 = []
        for a in str2:
            control_str2.append(a)
        for c in str1:
            for b in control_str2:
                if c == b:
                    control_str2.remove(b)
        return control_str1, control_str2

uso_strings = Strings()
control_str1, control_str2 = uso_strings.cadenax(selec1, selec2)
#print(control_str1)
#print(control_str2)


morsec = Archivos("Morse.txt")
morsecc = morsec.read()
#print(morsecc)

#SECCIÓN 2
class Morse():
    def __init__(self, textox):
        self.textox = textox
 
    def traduccion(self):
        traduc = []
        dicc = {"A": ".-",
                "B": "-…",
                "C": "-.-.",
                "D": "-…",
                "E": ".",
                "F": "…-.",
                "G": "--.",
                "H": "…",
                "I": "…",
                "J": ".—",
                "K": "-.-",
                "L": ".-…",
                "M": "–",
                "N": "-.",
                "Ñ": "--.–",
                "O": "—",
                "P": ".–.",
                "Q": "--.-",
                "R": ".-.",
                "S": "…",
                "T": "-",
                "U": "…-",
                "V": "…-",
                "W": ".–",
                "X": "-…-",
                "Y": "-.–",
                "Z": "--…"}
        for i in self.textox:
            for j in i:
                for key, value in dicc.items():
                    if j == key:
                        traduc.append(value)
        return traduc

uso_morse = Morse(textox)
traduc = uso_morse.traduccion()   
print(traduc) 
