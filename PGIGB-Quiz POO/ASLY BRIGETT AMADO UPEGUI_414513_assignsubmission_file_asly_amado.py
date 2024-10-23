import random
class Archivo():
    def __init__(self):
        self.ruta = ''
        self.info = []
    def leer(self,ruta=''):
        with open(ruta,'r',encoding='utf-8')as file:
            self.info = [i.strip() for i in file]

    def escribir(self,metodo,data,ruta= ''):
        if ruta== '':
            ruta = self.ruta
        with open(ruta,metodo,encoding='utf-8')as file:
                file.write(data+'/n')
    def cadena_aleatoria(self):
        data = self.info[0].split(',')
        elegido = random.choice(data)
        data.remove(elegido)
        self.info = [','.join(data)]
        return (elegido)

class String():
    def __init__(self,obj_archivo):
        self.cadena1= ''
        self.cadena2= ''
        self.out_1= []
        self.out_2= []
        self.obj_archivo = obj_archivo
    def cadenas_string(self,cad1,cad2):# self.cadena1= ''
        control=[]
        self.cadena1= cad1
        self.cadena2= cad2
        for i in self.cadena1:
            if i not in self.out_1:
                self.out_1.append(i)
        for j in self.cadena2:
            if j in self.out_1:
                self.out_1.remove(j)
                control.append(j)
            elif j not in control and j not in self.out_2:
                self.out_2.append(j)
        self.out_1= ''.join(self.out_1)
        self.out_2= ''.join(self.out_2)
        self.obj_archivo.escribir('w',f'{cad1+cad2};{cad1};{cad2};{self.out_1};{self.out_2}','Resultado.txt')
        #Strings;str1;str2;out1;out2

#         La salida uno (out1) debe contener los caracteres presentes en 
    # str1 pero que NO estén presentes en str2. - 
    # La salida dos (out2) debe contener los caracteres presentes en 
    # str2 pero NO estén presentes en str1
class Morse():
    def __init__(self,obj_archivo):
        self.traducido_morse = []
        self.texto_español= ''
        self.obj_archivo =obj_archivo

    def traduccion(self,texto):
        self.obj_archivo.leer('Morse.txt')
        traductor= self.obj_archivo.info
        dicc = {}
 

        for i in traductor:
            data = i.split(', ')
            dicc[data[0]] = data[1].strip("'")
        for letra in texto:
            if letra == ' ':
                self.traducido_morse.append('  ')
            elif letra == '.' and letra == ',':
                pass
            else:
                letra = letra.upper()
                if letra == 'á':
                    letra =  'A'
                elif letra == 'é':
                    letra =  'A'
                elif letra == 'í':
                    letra ='I'
                elif letra == 'ó':
                    letra = 'O'
                
                self.traducido_morse.append(dicc[letra])
                self.traducido_morse.append(' ')
        print(self.traducido_morse)
        self.obj_archivo.escribir('a',f'{''.join(self.traducido_morse)},{texto}','Resultado.txt')

        
def main():
    obj_archivo = Archivo()
    obj_archivo.leer('Texto.txt')
    cadena1= obj_archivo.cadena_aleatoria()
    cadena2= obj_archivo.cadena_aleatoria()
    obj_string = String(obj_archivo)
    obj_string.cadenas_string(cadena1,cadena2)
    obj_morse = Morse(obj_archivo)
    obj_morse.traduccion(obj_archivo.info[0])



if __name__=='__main__':
    main()