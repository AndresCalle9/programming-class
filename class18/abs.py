class Lavadora:
    def __init__(self,marca, carga):
        #atributos publicos
        self.marca = marca
        self.carga = carga
        #atributo privado
        self._litros = 12
    
    #metodos publicos
    def lavar(self, carga_lavado,temp='fria',en=1,cen=1):
        if carga_lavado < self.carga:
            self._llenar(temp)
            self._jabon()
            self._enjuagar(en)
            self._centrifugar(cen)
        else:
            print(f'No puede lavar carga superior a {self.carga}')

    #metodos privados
    def _llenar(self,temp):
        print(f'llenando tanque con {self._litros} Lts de agua {temp}')
    
    def _jabon(self):
        print('añadiendo jabón')

    def _enjuagar(self,ciclos):
        for i in range(ciclos):
            print('Enjuagando')

    def _centrifugar(self,ciclos):
        for i in range(ciclos):
            print('Centrifugando')
    

lav = Lavadora('LG',8)
lav.lavar(7,cen=2,en=9, temp = 'tibia')