import random

class Archivo:
    def _init_(self, filename):
        self.filename = filename
    
    def leer(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def escribir(self, data):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
    
    def random(self, nombre_archivo):
        contenido = self.leer(nombre_archivo)
        if contenido:
            return random.choice(contenido)
        else:
            return "El archivo está vacío."

class Esperanza:
    def escribir_resultados(self, numeros_fibonacci, numeros_armstrong):
        fibonacci_str = ", ".join(str(num) for num in numeros_fibonacci)
        resultados_armstrong = []
        for num in numeros_armstrong:
            if self.es_armstrong(num):
                resultados_armstrong.append(f"Armstrong, el número {num} es un número armstrong.")
            else:
                resultados_armstrong.append(f"Armstrong, el número {num} no es un número armstrong.")

        with open('resultados.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(f"Fibonacci, secuencia: {fibonacci_str}\n")
            for resultado in resultados_armstrong:
                archivo.write(resultado + "\n")

    def es_armstrong(self, numero):
        if numero < 10:
            return False
        
        numero_str = str(numero)
        num_digitos = len(numero_str)
        total = sum(int(digito) ** num_digitos for digito in numero_str) 
        
        return total == numero

    def generar_fibonacci(self, cantidad=100):
        fibonacci = []
        a, b = 0, 1
        for _ in range(cantidad):
            fibonacci.append(a)
            a, b = b, a + b
        return fibonacci

def main():
    esperanza = Esperanza()

    numeros_fibonacci = esperanza.generar_fibonacci()
    numeros_armstrong_input = input("Ingresa los números para verificar si son Armstrong: ").split(',')
    numeros_armstrong = []
    
    numeros_armstrong = [int(num) for num in numeros_armstrong_input if num.strip().isdigit()]
    esperanza.escribir_resultados(numeros_fibonacci, numeros_armstrong)

if __name__ == "_main_":
    main()
