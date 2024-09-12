
with open('./archivos/data.txt', 'r', encoding='utf-8') as file:
    data = file.read()

print(data)

nombres = ['Juan', 'Pedro', 'Maria', 'Ana', 'Jose', 'Luis', 'Carlos', 'Roberto', 'Ricardo', 'Javier']

with open('nombres.txt', 'w', encoding='utf-8') as file:
    for nombre in nombres:
        file.write(nombre + '\n')