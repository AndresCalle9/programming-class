import random
class Archivo:
    def __init__(self,ruta):
        self.ruta = ruta
        self.datos = []
    def leer(self):
        with open(self.ruta,"r", encoding="utf-8") as file:
            self.datos = [i.strip() for i in file]
    def escribir(self,metodo,datos):
        with open(self.ruta,metodo,encoding="utf-8") as file:
            file.write(datos + "\n")
    def aleatorio(self):
        for cadena in self.datos:
            aux = cadena.split(".")
            return random.choice(aux)
    
class Strings:
    def __init__(self):
        pass
    def cadena(self,srt1,str2):
        salida1 = []
        salida2 = []
        for i in srt1:
            salida1.append(i)
        for j in str2:
            salida2.append(j)
        output1 = []
        for let in salida1:
            if let not in salida2 and let not in output1:
                output1.append(let)
        output2 = []
        for let2 in salida2:
            if let2 not in salida1 and let2 not in output2:
                output2.append(let2)
        out1 = "".join(output1)
        out2 = "".join(output2)
        return out1,out2

class Morse:
    def __init__(self,texto):
        self.texto =texto
    def traduccion(self,letras_morse):
        traduc = []
        for letra in self.texto:
            if letra == " ":
                    traduc.append(" ")
            for i in letras_morse:
                aux = i.split(",")
                if letra == aux[0]:
                    traduc.append(aux[1])
                
        traduc_final = "".join(traduc)
        return(traduc_final)

texto = Archivo("texto.txt")
texto.leer()
cadena_aleatoria1 = texto.aleatorio().upper()
cadena_aleatoria2 = texto.aleatorio().upper()
if cadena_aleatoria2 == cadena_aleatoria1:
    cadena_aleatoria2 = texto.aleatorio().upper()
print(cadena_aleatoria1)
print("-------------------------")
print(cadena_aleatoria2)
strings = Strings()
out1,out2 =strings.cadena(cadena_aleatoria1,cadena_aleatoria2)
resultados = Archivo("resultados.txt")
resultados.escribir("a", f"Strings; STR1:{cadena_aleatoria1}; STR2:{cadena_aleatoria2}; OUT1:{out1}; OUT2:{out2}")
archivo_morse = Archivo("morse.txt")
archivo_morse.leer()
datos = archivo_morse.datos
texto_completo = "".join(texto.datos).upper()
morse = Morse(texto_completo)
texto_traducido = morse.traduccion(datos)
print(texto_traducido)
resultados.escribir("a", f"Texto:{texto.datos}; Morse: {texto_traducido}")
