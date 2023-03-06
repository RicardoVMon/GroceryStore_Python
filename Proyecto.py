# productos (Pulpería)

lays = 500
huevos = 1200
gaseosa = 1000
tortillas = 400
hersheys = 800

cantidad_lays = 7
cantidad_huevos = 5
cantidad_gaseosa = 9
cantidad_tortillas = 15
cantidad_hersheys = 2



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

        print('-'*24+'MENÚ DE PRODUCTOS'+'-'*24)
        print('[1] - Lays\n[2] - Huevos\n[3] - Gaseosa\n[4] - Tortilla\n[5] - Hersheys')
        
        opcion_producto = input('Digite el número de producto que desea comprar: ')
        cantidad_producto = input('Digite la cantidad que desea comprar de ese producto: ')



    elif eleccion == '2':
        
        print('Gracias por usar nuestro sistema')
        loop = False
    
    else:
        print('\nPor favor, ingrese una opción válida\n')
