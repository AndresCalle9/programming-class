import random

class Archivo():
    def __init__(self, ruta):
        self.ruta = ruta
        self.info = []
        
    def read(self):
        with open(self.ruta, "r", encoding="utf-8") as file:
            self.info = [line.strip() for line in file]
        self.headers = self.info[0]
    
    def write(self, method, ruta_aux = "", datos = []):
        if ruta_aux == "":
            ruta_aux = self.ruta
        if len(datos) == 0:
            datos = self.info
        with open(ruta_aux, method, encoding="utf-8") as file:
            if method == "w":
                for line in datos:
                    file.write(line+"\n")

    def random(self):
        if self.info:
            return random.choice(self.info)
        return None

class Strings():
    def __init__(self, strings = []):
        self.strings = strings
        
    def procesar(self, str1, str2):
        
        out1 = ''.join([caracter for caracter in str1 if caracter not in str2])
        out2 = ''.join([caracter for caracter in str2 if caracter not in str1])
    
        return out1, out2

def main():
    archivo = Archivo('texto.txt')
    archivo.read()

    str1 = archivo.info[0]
    str2 = archivo.random() if len(archivo.info) > 1 else str1
    out1, out2 = Strings.procesar(archivo, str1, str2)
    resultado = Archivo("./resultado.txt")
    resultado.write("w", datos=[f"Strings;{str1};{str2};{out1};{out2}"])

if __name__ == "__main__":
    main()