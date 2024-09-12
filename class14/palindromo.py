# def palindromo(pal):
#     pal_inv = pal[::-1]
#     if pal == pal_inv:
#         return True
#     else:
#         return False

# def palindromo(pal):
#     return pal == pal[::-1]

palindromo = lambda pal:pal == pal[::-1]

def main():
    pal = input('Ingrese una palabra: ')
    result = palindromo(pal)
    if result:
        print('si es')
    else:
        print('no es')

if __name__ == '__main__':
    main()