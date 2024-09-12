def read(ruta):
    with open(ruta,'r', encoding='utf-8') as file:
        datos = [line.strip() for line in file]
    return datos

def write(ruta,metodo,datos):
    with open(ruta, metodo, encoding='utf-8') as file:
        for i in datos:
            file.write(i+'\n')

def get_by_category(datos):
    data_category = {}
    for i in range(1,len(datos)):
        category = datos[i].split(',')[1]
        if category not in data_category:
            data_category[category] = []
        data_category[category].append(datos[i])
    return data_category

def search_all(datos, col):
    return [i.split(',')[col] for i in datos]

def add_product(datos):
    cont = 0
    while cont < 5:
        ids = search_all(datos,0)
        id = input('Ingrese el id del producto: ')  
        if id in ids:
            print('Ingrese un id no existente')
        else:
            categoria = input('Ingrese la categoria del producto: ')
            nombre = input('Ingrese el nombre del producto: ')
            precio = input('Ingrese el precio del producto: ')
            descripcion = input('Ingrese la descripcion del producto: ')
            stock = input('Ingrese el stock del producto: ')
            datos.append(f'{id},{categoria},{nombre},{descripcion},{precio},{stock}')
            cont += 1
    return datos

def add_users(target,usuarios = []):
    cont = 0
    while cont < target:
        nombres = search_all(usuarios,0)
        nombre = input('Ingrese el nombre del usuario: ')
        if nombre in nombres:
            print('Ingrese un nombre no existente')
        else:
            contrasena = input('Ingrese la contrasena del usuario: ')
            while len(contrasena) < 4:
                print('Ingrese una contrasena mayor a 4 caracteres')
                contrasena = input('Ingrese la contrasena del usuario: ')
            presupuesto = input('Ingrese el presupuesto del usuario: ')
            usuarios.append(f'{nombre},{contrasena},{presupuesto}')
            cont += 1

    return usuarios

def login(usuarios,nombre):
    cont_rep = 0
    while True:
        nombres = search_all(usuarios,0)
        contrasenas = search_all(usuarios,1)

        if nombre in nombres:
            contrasena = input('Ingrese la contrasena: ')
            index = nombres.index(nombre)
            if contrasena == contrasenas[index]:
                return True, None
            else:
                print('Contrasena incorrecta')
                return False, None
        else:
            print('Usuario no registrado')
            cont_rep += 1
            if cont_rep > 1:
                opt = input('Desea registrarse? (si/no): ')
                if opt == 'si':
                    return True, add_users(1,usuarios)
                else:
                    break

    
    return False, None

def comprar(datos, usuarios,nombre):
    cantidad = int(input('Ingrese la cantidad de productos a comprar: '))
    presupuesto = [int(i.strip().split(',')[2]) for i in usuarios if i.strip().split(',')[0] == nombre][0]
    id = input('Ingrese el id del producto: ')
    ids = search_all(datos,0)
    if id in ids:
        index = ids.index(id)
        stock = int(datos[index].split(',')[5])
        valor = int(datos[index].split(',')[4])
        if presupuesto > cantidad*valor and cantidad < stock:
            return True, [f'{nombre},{id},{cantidad},{cantidad*valor},{presupuesto-cantidad*valor},2021-10-10']
    else:
        print('Producto no encontrado')
        return False, None
    
    return False, None



def main():
    datos = read('marketPlace.txt')
    datos_category = get_by_category(datos)
    # 1.a
    for key in datos_category:
        for i in datos_category[key]:
            print(key,i.split(',')[0], i.split(',')[2])
    # 1.b        
    # datos_actualizados = add_product(datos)
    # write('marketPlace.txt','w',datos_actualizados)
    # 2.a
    # usuarios = add_users(3)
    # write('users.txt','w',['nombre,contrasena,presupuesto'])
    # write('users.txt','a',usuarios)
    #2.b
    usuarios = read('users.txt')
    nombre = input('Ingrese el nombre de usuario: ')
    result, usuarios_actualizados = login(usuarios,nombre)
    if usuarios_actualizados:
        write('users.txt','w',usuarios_actualizados)
    
    if result:
        #3.a
        write('registros.txt','w',['nombre usuario,id,cantidad,valor,saldo,fecha'])
        result, registros = comprar(datos,usuarios,nombre)
        if result:
            #3.b
            write('registros.txt','a',registros)
        else:
            print('No se pudo realizar la compra verifique sus parámetros')
    else:
        print('No inició sesión correctamente')
        nombre = input('Ingrese el nombre de usuario: ')
        login(usuarios,nombre)






if __name__ == '__main__':
    main()