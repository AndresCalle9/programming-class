import random 
class Archivo:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo 
        self.contenido = None  


    def leer(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.contenido = archivo.read() 
            return self.contenido
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{self.ruta_archivo}'")  
            return None
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")  
            return None


    def escribir(self, texto):
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(texto) 
            print(f"Texto escrito en el archivo '{self.ruta_archivo}'")
        except Exception as e:
            print(f"Ocurrió un error al escribir en el archivo: {e}")  

    def random(self):
        if self.contenido is None:  
            self.leer()  
        if self.contenido:  
            palabras = self.contenido.split()  
            return random.choice(palabras) if palabras else None  
        else:
            return None  

archivo = Archivo('texto.txt')
archivo.escribir("Andres es muy buen profesor y kamila va ha pasar este examen .")
print(archivo.leer())
print(archivo.random())


import random

class Esperanza:
    def fibonacci(self):
        secuencia = [0, 1] 
        while len(secuencia) < 100:
            siguiente = secuencia[-1] + secuencia[-2]
            secuencia.append(siguiente)
        return secuencia
    
    def armstrong(self, numero):
        digitos = [int(d) for d in str(numero)]
        suma = sum([d**3 for d in digitos])
        return suma == numero


def escribir_resultado(archivo, tipo, mensaje):
    with open(archivo, 'a', encoding='utf-8') as f:
        f.write(f"{tipo}, {mensaje}\n")


esperanza = Esperanza()


fibonacci_100 = esperanza.fibonacci()


escribir_resultado('resultado.txt', 'Fibonacci', ', '.join(map(str, fibonacci_100)))


numeros_aleatorios = random.sample(fibonacci_100, 5)


for numero in numeros_aleatorios:
    if esperanza.armstrong(numero):
        escribir_resultado('resultado.txt', 'Armstrong', f"el número {numero} es un número armstrong")
    else:
        escribir_resultado('resultado.txt', 'Armstrong', f"el número {numero} no es un número armstrong")


numero_especial = 153
if esperanza.armstrong(numero_especial):
    escribir_resultado('resultado.txt', 'Armstrong', f"el número {numero_especial} es un número armstrong")
else:
    escribir_resultado('resultado.txt', 'Armstrong', f"el número {numero_especial} no es un número armstrong")