import random

def read(ruta):
    with open(ruta, 'r', encoding='utf-8') as file:
        output = [line.strip() for line in file]

    return output

def save_word(palabra):
    return ['-' for letra in palabra]

def main():
    data = read('./archivos/data.txt')
    print(data)
    pal_secreta = random.choice(data) # Selecciona una palabra al azar
    print(pal_secreta)
    pal_secreta_oculta = save_word(pal_secreta)
    print(pal_secreta_oculta)
    
if __name__ == '__main__':
    main()