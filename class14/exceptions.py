# def divisors(num):
#     divisores = []
#     if num < 0:
#         raise ValueError
#     for i in range(1,num +1):
#         if num % i == 0:
#             divisores.append(i)
#     return divisores

# def main():
#     try:
#         num = int(input('Ingrese un número: '))
#         lista = divisors(num)
#         print(lista)
#     except ValueError as ve:
#         print('Ingrese un número positivo')
#     except ZeroDivisionError as zde:
#         print('No puede dividir por 0')
#     except:
#         print('hola')

# if __name__ == '__main__':
#     main()

def divisors(num):
    divisores = []
    if num < 0:
        raise ValueError('número debe ser positivo')
    for i in range(1,num +1):
        if num % i == 0:
            divisores.append(i)
    return divisores

def main():
    try:
        num = int(input('Ingrese un número: '))
        lista = divisors(num)
        print(lista)
    except ValueError as ve:
        print('Error: ', ve)
    except ZeroDivisionError as zde:
        print('Error: ', zde)
    except:
        print('hola')
    finally:
        print('finally')

if __name__ == '__main__':
    main()