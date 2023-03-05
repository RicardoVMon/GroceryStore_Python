def menu_principal():
    print('1) Ingresar nueva compra\n2) Salir')
    eleccion = input('\nSeleccione la opción de su preferencia: ')
    return eleccion


print('\nBienvenido a la tienda "Los Pollitos"\n')
loop = True
while loop:
    eleccion = menu_principal()
    if eleccion == '1':
        print('Selección 1')
        break
    elif eleccion == '2':
        print('Gracias por usar nuestro sistema')
        break
    else:
        print('\nPor favor, ingrese una opción válida\n')
