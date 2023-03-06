# productos (Pulpería)

lays = 500
huevos = 1200
gaseosa = 1000
tortillas = 400
hersheys = 800
cantidad_productos = 0


# bienvenida
print('\nBienvenido a la tienda "Los Pollitos"\n')

# loop principal
loop = True
while loop:
    print('1) Ingresar nueva compra\n2) Salir')
    eleccion = input('\nSeleccione la opción de su preferencia: ')

    if eleccion == '1':
        
        nombre_cliente = input('Por favor, ingrese su nombre: ')

        if nombre_cliente == '':
            print('¡ERROR! El espacio de nombre no puede estar en blanco, inténtelo de nuevo.')

        dia_compra = input('Por favor, ingrese el número de día de su compra: ')
        # validación día no mayor a 31

        mes_compra = input('Por favor, ingrese el número de mes de su compra: ')
        # validación mes no mayor a 12
        
        año_compra = input('Por favor, ingrese el año de su compra: '+'\n')

        print('-'*24+'MENÚ DE PRODUCTOS'+'-'*24)
        print('[1] - Lays\n[2] - Huevos\n[3] - Gaseosa\n[4] - Tortilla\n[5] - Hersheys')
        
        opcion_producto = input('Digite el número de producto que desea comprar: ')
        cantidad_producto = input('Digite la cantidad que desea comprar de ese producto: ')



    elif eleccion == '2':
        
        print('Gracias por usar nuestro sistema')
        loop = False
    
    else:
        print('\nPor favor, ingrese una opción válida\n')
