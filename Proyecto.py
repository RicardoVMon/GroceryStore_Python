""" 
Falta validar el máximo de productos que se compran
Si es que sólo se puede volver a comprar hasta 20 veces, variable de contador y cerrar ciclo
Si es que sólo 20 productos en general, variable que lleve cantidad de productos y cerrar ciclo
"""

# productos (Pulpería)

precio_lays = 500
precio_huevos = 1200
precio_gaseosa = 1000
precio_tortillas = 400
precio_hersheys = 800
contador_productos = 0
total_bruto = 0


# bienvenida
print('\nBienvenido a la tienda "Los Pollitos"\n')

# loop principal
loop = True
while loop:
    print('1) Ingresar nueva compra\n2) Salir')
    eleccion = input('\nSeleccione la opción de su preferencia: ')

    if eleccion == '1':
        
        # ciclo para validar nombre
        preguntar_nombre = True
        while preguntar_nombre:
            nombre_cliente = input('\nPor favor, ingrese su nombre: ')
            if nombre_cliente == "":
                print('\n¡ERROR! El nombre no puede estar vacío')
            else:
                preguntar_nombre = False
        
        # ciclo para validar que día sea menor a 31
        preguntar_dia = True
        while preguntar_dia:
            dia_compra = int(input('\nPor favor, ingrese el número de DÍA de su compra (1-31): '))
            if dia_compra > 31 :
                print('\n¡ERROR! El mes no tiene más de 31 días')
            else:
                preguntar_dia = False

        # ciclo para validar que meses no sean mayores a 12
        preguntar_mes = True
        while preguntar_mes:
            mes_compra = int(input('\nPor favor, ingrese el número de MES de su compra (1-12): '))
            if mes_compra > 12:
                print('\n¡ERROR! El año no tiene más de 12 meses')
            else:
                preguntar_mes = False
        
        # ciclo para validar que año sea mayor a 2022
        preguntar_annio = True
        while preguntar_annio:
            annio_compra = int(input('\nPor favor, ingrese el AÑO de su compra (Mayor a 2022): '))
            if annio_compra < 2023:
                print('\n¡ERROR! El año debe ser mayor a 2022')
            else:
                preguntar_annio = False

        # mostrar menú de productos 
        mostrar_menu = True
        while mostrar_menu:  
            print('\n' + '-'*24+'MENÚ DE PRODUCTOS'+ '-'*24)
            print('\n[1] - Lays\n[2] - Huevos\n[3] - Gaseosa\n[4] - Tortilla\n[5] - Hersheys')
        
            # preguntar datos de productos
            opcion_producto = input('\nDigite el número de producto que desea comprar: ')
            cantidad_producto = int(input('\nDigite la cantidad que desea comprar de ese producto: '))

            # cálculo según producto
            if opcion_producto == '1':
                total_bruto += precio_lays * cantidad_producto
            
            elif opcion_producto == '2':
                total_bruto += precio_huevos * cantidad_producto

            elif opcion_producto == '3':
                total_bruto += precio_gaseosa * cantidad_producto
            
            elif opcion_producto == '4':
                total_bruto += precio_tortillas * cantidad_producto
            
            elif opcion_producto == '5':
                total_bruto += precio_hersheys * cantidad_producto

            # preguntar si quiere añadir otro producto
            print('\n¿Desea agregar un nuevo producto?\n\n[1] - Sí\n[2] - No\n')
            continuar = input('Digite la opción de su preferencia: ')
            if continuar == '1':
                print('\nContinuando compra...\n')
            elif continuar == '2':
                print('\nCerrando menú de productos...\n')
                mostrar_menu = False
            else:
                print('\n¡ERROR! Digite una opción válida!\n')

    elif eleccion == '2':
        
        print('\nGracias por usar nuestro sistema\n')
        loop = False
    
    else:
        print('\nPor favor, ingrese una opción válida\n')
