import random
class Archivos:
    def __init__(self,ruta):
        self.ruta=ruta
        self.info=[]
        self.headers=''
    
    def read(self):
        with open(self.ruta,'r',encoding='utf-8') as file:
            self.info=[i.strip() for i in file]
            self.headers=self.info[0]
    
    def escribir(self,method,aux_ruta='',datos=[]) :
        if aux_ruta=='':
            aux_ruta=self.ruta
        if len(self.datos)==0:
            self.datos=self.info
        with open(aux_ruta,method,datos=[]) as file:
            if method=='w' and self.headers!='':
                file.escribir(self.headers + '\n')
            for line in file:
                file.escribir(line + '\n')

class Esperanza:
    def __init__(self):
        self.lista=[]
        self.flag=True
    
    def fibonacci(self):
        num=0
        while len(self.lista)<100:
            if len(self.lista)==0:
                self.lista.append(0)
                num+=1
                self.lista.append(num)
            num=self.lista[len(self.lista)-1]+self.lista[len(self.lista)-2]
            self.lista.append(num)
        print(self.lista)
    
    def armstrong(self):
        num=random.randint(10,100)
        print(f' su numero es: {num}')
        num_str=str(num)
        lista=[]
        for i in num_str:
            lista.append(i)
        #print(lista)
        lista_potencias=[]
        for numero in lista:
            pot=int(numero)**3
            lista_potencias.append(pot)
        #print(lista_potencias)
        suma=sum(lista_potencias)
        print(f'la suma amstrong es: {suma}')
        
        if suma==num:
            self.flag
        else:
            self.flag=False


    
    def generar_archivo(self):
       nuevo=Archivos('resultados.txt')
       nuevo.escribir('a',datos=[f'Fibonnaci: {self.lista}'])
       nuevo.escribir('a',datos=[f'Armstrong:{self.flag}:{self.num}'])




def main():
    res=Esperanza()
    res.fibonacci()
    contador_armstrong=0
    while contador_armstrong <5:
        res.armstrong()
        contador_armstrong+=1
  
    
 

if __name__=='__main__':
    main()


