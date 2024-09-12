# crear una función que calcule el IMC en Kg/m^2 y considere conversiones

def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def conv_peso(peso):
    resultado = peso/1000
    return resultado

def conv_altura(altura):
    resultado = altura/100
    return resultado

def clasif_imc(imc):
    mensaje = ''
    if imc < 18.5:
        mensaje = 'Bajo peso'
    elif imc >= 18.5 and imc < 24.9:
        mensaje = 'Normal'
    elif imc >= 24.9 and imc < 29.9:
        mensaje = 'Sobrepeso'
    else:
        mensaje = 'Obesidad'

    return mensaje


def main():
    peso = 72 #float(input('Ingrese su peso: '))
    altura = 183 #float(input('Ingrese su altura: '))

    if peso > 1000:
        peso = conv_peso(peso)
    
    if altura > 10:
        altura = conv_altura(altura)
    
    imc_calculado = imc(peso, altura)
    print(imc_calculado)
    clasificacion = clasif_imc(imc_calculado)
    print(clasificacion)

if __name__ == '__main__':
    main()