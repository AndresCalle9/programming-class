class Obj:

    def __init__(self):
        self.numeros = [i for i in range(0,1000)]
        self.par = []
        self.impar = []

    def dividir(self):
        for i in self.numeros:
            if i % 2 == 0:
                self.par.append(i)
            else:
                self.impar.append(i)


numeros = Obj()
print(numeros.par)
numeros.dividir()

print(numeros.par)