def divisors(num):
    divisores = []
    num = int(num)
    for i in range(1,num +1):
        if num % i == 0:
            divisores.append(i)
    return divisores

def main():
    num = input('Ingrese un número: ')
    assert num.isnumeric(), 'Debes ingresar un número'
    lista = divisors(num)
    print(lista)
    

if __name__ == '__main__':
    main()