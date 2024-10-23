import random

class Archivos():
    def __init__(self, ruta):
        self.ruta = ruta
        self.info = []
        self.headers = ''
    
    def read(self):
        with open(self.ruta,'r', encoding='utf-8') as file:
            self.info = [i.strip() for i in file]
        self.headers = self.info[0]
        self.info.pop(0)

    def write(self, method, ruta_aux='', datos = []):
        if ruta_aux == '':
            ruta_aux = self.ruta
        if len(datos) == 0:
            datos = self.info
        with open(ruta_aux,method,encoding='utf-8') as file:
            if method == 'w' and self.headers != '':
                file.write(self.headers + '\n')
            for line in datos:
                file.write(line + '\n')
    
    def search_one(self,target,col,separator):
        for idx, value in enumerate(self.info):
            aux = value.split(separator)
            if aux[col] == target:
                return idx
        
        return False
    
    def search_all(self,target,col,separator):
        output = []
        for idx, value in enumerate(self.info):
            aux = value.split(separator)
            if aux[col] == target:
                output.append(idx)
        
        return output
    
    def filter_uniques(self,col,separator):
        output = []
        [ output.append(x.split(separator)[col]) for x in self.info if x.split(separator)[col] not in output ]
        return output

class Equipo:
    def __init__ (self,nombre,jugadores):
        self.nombre_equipo = nombre
        self.jugadores = jugadores
        self.set_ganados = 0

    def anotar(self):
        anotador = random.choice(self.jugadores)
        anotador.convertir()
    
    def agregar_jugador(self,aux):
        self.jugadores.append(aux)
    
    def puntaje(self):
        sum = 0
        for i in self.jugadores:
            sum += i._puntos
        return sum
    
    def ganar_set(self):
        self.set_ganados += 1
    
    def limpiar_puntos(self):
        for jugador in self.jugadores:
            jugador._puntos = 0



class Jugador(Equipo):
    def __init__(self, nombre, numero, posicion, nombre_equipo):
        super().__init__(nombre_equipo,[])
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion
        self._puntos = 0
    
    def convertir(self):
        self._puntos += 1
        print(f'{self.nombre} ha anotado un punto para el equipo {self.nombre_equipo}')
    
class Game:
    def __init__(self,equipo_a, equipo_b):
        self.equipos =[equipo_a,equipo_b]
        self.set_juego = 1
    
    def set(self):
        if (self.set_juego < 5):
            umbral = 25
        else:
            umbral = 15
        
        self.equipos[0].limpiar_puntos()
        self.equipos[1].limpiar_puntos()
        while self.equipos[0].puntaje() < umbral and self.equipos[1].puntaje() < umbral:
            equipo_anotador = random.choice(self.equipos)
            equipo_anotador.anotar()
            print(f'el marcador va: {self.equipos[0].nombre_equipo} : {self.equipos[0].puntaje()} VS {self.equipos[1].nombre_equipo} : {self.equipos[1].puntaje()}')
        
        if self.equipos[0].puntaje() > self.equipos[1].puntaje():
            self.equipos[0].ganar_set()
        else:
            self.equipos[1].ganar_set()
        
        self.set_juego +=1




def crear_equipo(obj_arch,nombre_equipo):
    posiciones = obj_arch.filter_uniques(2,',')
    equipo = Equipo(nombre_equipo,[])
    while len(equipo.jugadores) < 6:
        idx = obj_arch.search_one(posiciones[len(equipo.jugadores)],2,',')
        aux = obj_arch.info[idx].split(',')
        jugador = Jugador(aux[0], aux[1], aux[2],nombre_equipo)
        equipo.agregar_jugador(jugador)
        obj_arch.info.pop(idx)
    return equipo



def main():
    obj = Archivos('./class21/jugadores.txt')
    obj.read()

    equipo_1 = crear_equipo(obj,'Medellin')
    equipo_2 = crear_equipo(obj,'Nacional')

    juego = Game(equipo_1,equipo_2)

    while equipo_1.set_ganados < 3 and equipo_2.set_ganados < 3:
        print(f'------------ Set {juego.set_juego} -----------')
        juego.set()
    print(f'{equipo_1.nombre_equipo}:{equipo_1.set_ganados} VS {equipo_2.nombre_equipo}:{equipo_2.set_ganados}')


if __name__ == '__main__':
    main()

