import random

class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.info = []
        self.headers = ''
    
    def read(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as file:
                self.info = [linea.strip() for linea in file.readlines()]
            self.headers = self.info[0] if self.info else ''
            if self.info:
                self.info.pop(0)  # Eliminar el encabezado si existe
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta}' no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    
    def write(self, mode, ruta_aux='', datos=[]):
        if ruta_aux == '':
            ruta_aux = self.ruta
        if len(datos) == 0:
            datos = self.info
        with open(ruta_aux, mode=mode, encoding='utf-8') as file:
            if mode == 'w' and self.headers != '':
                file.write(self.headers + '\n')
            for line in datos:
                file.write(line + '\n')

    def random(self):
        if self.info:
            return random.choice(self.info)
        else:
            return None


class Strings:
    def comparar(self, str1, str2, archivo):
        out1 = ''.join([char for char in str1 if char not in str2])
        out2 = ''.join([char for char in str2 if char not in str1])
        resultado = f"Strings;{str1};{str2};{out1};{out2}"
        archivo.write('a', datos=[resultado])
        return out1, out2


class Morse(Archivo):
    def traduccion(self, texto):
        archivo_morse = Archivo('Morse.txt')
        archivo_morse.read()
        
        morse_dict = {}
        for linea in archivo_morse.info:
            letra, codigo = linea.strip().split(', ')
            morse_dict[letra] = codigo

        texto_traducido = []
        for palabra in texto.split(' '):
            palabra_traducida = ' '.join(morse_dict.get(letra.upper(), '') for letra in palabra)
            texto_traducido.append(palabra_traducida)
        morse_traducido = '  '.join(texto_traducido)  # Dos espacios entre palabras

        return morse_traducido


archivo_texto = Archivo('Texto.txt')
archivo_texto.read()

if archivo_texto.info:
    str1 = archivo_texto.info[0] 
else:
    str1 = ''  

str2 = ''  

strings = Strings()
resultados_archivo = Archivo('resultados.txt')
out1, out2 = strings.comparar(str1, str2, resultados_archivo)
print(f"Out1: {out1}")
print(f"Out2: {out2}")

morse = Morse('resultados.txt')

if archivo_texto.info:
    texto_original = ' '.join(archivo_texto.info) 
    morse_traducido = morse.traduccion(texto_original)
    resultado_morse = f"Morse, {morse_traducido}"
    resultados_archivo.write('a', datos=[resultado_morse])
    print(f"Texto traducido a Morse:\n{morse_traducido}")
else:
    print("El archivo 'texto.txt' está vacío.")

