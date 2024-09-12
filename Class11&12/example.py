#Nested - Anidamiento

# count = 0
# for i in range(5): #0,1,2,3,4
#     for j in range(4):#0,1,2,3
#         print(i,j)
#         count += 1

# print (count)


# inicio - todas
# adelante - atras o derecha
# izq - adelante o atras
# der - izq o adelante
# atras - todas

menu = '''
Ingrese la dirección en la que le gustaría avanzar:
1) Adelante
2) Izq
3) Atras
4) Der

'''

def second_decision(menu,opt_1):
    print(menu)
    opt_2 = input('Seleccione un número: ')
    if opt_2 == '1':
        ways = menu.split('1)')
        way_2 = ways[1].split('2)')[0]
    else:
        ways = menu.split('2)')
        way_2 = ways[1] 
    return(f'Avanzaste primero hacia {opt_1} y luego {way_2}')


print(menu)
opt = input('Seleccione un número: ')


while True:
    if opt == '1':
        menu_ad = '''
            Ingrese una nueva opción:

            1) Atras 
            2) Der
            '''
        response = second_decision(menu_ad,'Adelante') 
    elif opt == '2':
        menu_izq = '''
            Ingrese una nueva opción:

            1) Adelante 
            2) Atras
            '''
        response = second_decision(menu_izq,'Izq')
    else:
        break

    print(response)
    print(menu)
    opt = input('Seleccione un número: ')


#A Adelante
#Z Atras
#I izq
#D der
treasure = ['D','A','D','I','A','I','Z','D','I']
treasure_2 = 'DADIAIZDI'