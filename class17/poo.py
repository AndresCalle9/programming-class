class Carro:
    llantas = 4 #otra forma de asignar valores por defecto forma 2
    #Atributos - estática del obj
    #Constructor
    def __init__(self, color, marca, modelo, ace, serie, puertas = 4): # puertas es la forma 3 de valores por defecto
        #Asignar los atributos
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.aceleracion = ace
        self.velocidad  = 0 #asignar un atriburo por defecto forma 1
        self.puertas = puertas
        self.serie = serie

    #métodos - dinámica del obj
    def acelerar(self):
        self.velocidad += self.aceleracion
    
    def frenar(self):
        self.velocidad -= self.aceleracion

#instanciar una clase
carro1 = Carro('azul','chevrolet',2024,50,'tracker') # carro1 es una instancia de clase Carro

print(carro1.color)
print(carro1.velocidad)
print(carro1.aceleracion)

carro2 = Carro('gris','renault',2017,100,'sandero',5)

print(carro2.color)
print(carro2.velocidad)
print(carro2.aceleracion)
print(carro2.llantas)

print(carro1.puertas, carro2.puertas)
print(carro1.serie, carro2.serie)

print(carro1.velocidad)
carro1.acelerar()
print(carro1.velocidad)
carro1.acelerar()
carro1.frenar()
print(carro1.velocidad)

# print(carro2.velocidad)
# carro2.acelerar()
# print(carro2.velocidad)
# carro2.acelerar()
# print(carro2.velocidad)