# Importaciones

# Funciones auxiliares
def count_find(parr, target):
    total = parr.count(target)
    lista = []
    for idx, i in enumerate(parr):
        if i == target:
            lista.append(idx)
    
    return total, lista

# Función principales
def main():
    parrafo = 'Lorem ipsum dolor sit amet consectetur adipiscing elit rhoncus arcu dignissim, magna at turpis volutpat faucibus vulputate interdum cursus placerat, accumsan commodo facilisis ultrices nascetur erat metus pharetra tincidunt. Tempor at nam placerat aliquam aenean luctus libero ad orci, condimentum mattis vel interdum porta morbi posuere tristique, cursus fringilla malesuada cras massa justo bibendum felis. Purus tempus neque rhoncus facilisis lacus laoreet parturient ad lobortis semper vivamus, tristique turpis nisl vehicula ornare fringilla feugiat vitae primis montes, suspendisse magna posuere mauris cum rutrum diam id potenti nisi. Eleifend varius vitae sagittis primis porttitor duis ullamcorper, aliquet platea posuere mus vivamus nullam, a arcu dui feugiat fusce sociis. Ultricies nisi libero ridiculus lacinia luctus imperdiet nisl, dignissim massa molestie duis cubilia venenatis, sem nullam natoque eleifend augue varius. Luctus varius nec sodales convallis scelerisque natoque, egestas justo sed mollis dis parturient inceptos, phasellus venenatis dui lacinia mus.'
    cantidad , indices = count_find(parrafo, 'a')
    print('Cantidad de "a":',cantidad)
    print('Indices:',indices)
    
# Punto de entrada - Entry point
if __name__ == '__main__':
    main()
