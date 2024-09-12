def read(ruta):
    output = []
    with open(ruta, 'r', encoding='utf-8') as file:
        for line in file:
            output.append(line.strip())
    return output

def write(ruta, method, data):
    with open(ruta, method, encoding='utf-8') as file:
        for i in data:
            file.write(i + '\n')

def main():
    data = read('./archivos/data.txt')
    print(data, type(data))
    data = read('nombres.txt')
    print(data, type(data))
    write('nombres2.txt','a', ['Juan', 'Pedro', 'Maria', 'Ana', 'Jose', 'Luis', 'Carlos', 'Roberto', 'Ricardo', 'Javier'])
    write('./archivos/nombres.txt','w',['Andrés'])

if __name__ == '__main__':
    main()