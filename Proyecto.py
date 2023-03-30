def validarNombre():

    preguntar_nombre = True
    while preguntar_nombre:
        nombre_cliente = input('\nPor favor, ingrese su nombre: ')
        if nombre_cliente == "":
            print('\n¡ERROR! El nombre no puede estar vacío')
        else:
            preguntar_nombre = False
    
    return nombre_cliente
def validarDia():
    preguntar_dia = True
    while preguntar_dia:
        dia_compra = int(input('\nPor favor, ingrese el número de DÍA de su compra (1-31): '))
        if dia_compra > 31 :
            print('\n¡ERROR! El mes no tiene más de 31 días')
        else:
            preguntar_dia = False
    
    return dia_compra
def validarMes():
    preguntar_mes = True
    while preguntar_mes:
        mes_compra = int(input('\nPor favor, ingrese el número de MES de su compra (1-12): '))
        if mes_compra > 12:
            print('\n¡ERROR! El año no tiene más de 12 meses')
        else:
            preguntar_mes = False
    
    return mes_compra
def validarAnnio():
    preguntar_annio = True
    while preguntar_annio:
        annio_compra = int(input('\nPor favor, ingrese el AÑO de su compra (Mayor a 2022): '))
        if annio_compra < 2023:
            print('\n¡ERROR! El año debe ser mayor a 2022')
        else:
            preguntar_annio = False


# productos (Pulpería)
precio_lays = 500
precio_huevos = 1200

# bienvenida
print('\nBienvenido a la tienda "Los Pollitos"\n')

# loop principal
loop = True
while loop:
    
    # variables de totales en 0
    total_bruto = 0
    total_huevos = 0
    total_lays = 0

    # variables de selección de productos
    escogio_huevos = False
    escogio_lays = False
    limite_alcanzado = False
    agregar_nuevo = True
    
    print('1) Ingresar nueva compra\n2) Salir')
    eleccion = input('\nSeleccione la opción de su preferencia: ')

    if eleccion == '1':
        
        # ciclo para validar nombre
        nombre_cliente = validarNombre()
        
        # ciclo para validar que día sea menor a 31
        dia_compra = validarDia()

        # ciclo para validar que meses no sean mayores a 12
        mes_compra = validarMes()
        
        # ciclo para validar que año sea mayor a 2022
        annio_compra = validarAnnio()

        # mostrar menú de productos 
        mostrar_menu = True
        while mostrar_menu:  
            print('\n' + '*'*24+' MENÚ DE PRODUCTOS '+ '*'*24)
            print('\n[1] - Papas Lays: ₡500\n[2] - Kg de huevos: ₡1200')
            
            # preguntar datos de productos
            opcion_producto = int(input('\nDigite el número de producto que desea comprar: '))
            
            if opcion_producto in range(1,3):
                cantidad_producto = int(input('\nDigite la cantidad que desea comprar de ese producto: '))

               # calculos de opcion y cantidad
                if opcion_producto == 1:
                    total_lays += precio_lays * cantidad_producto
                    escogio_lays = True
                elif opcion_producto == 2:
                    total_huevos += precio_huevos * cantidad_producto
                    escogio_huevos = True
                
                # si se compraron de los 2 tipos, se cierra ciclo
                if escogio_lays == True and escogio_huevos == True:
                    limite_alcanzado = True
                
                # llevar cuenta del total bruto
                total_bruto = total_lays + total_huevos

                # si se alcanza límite de productos, se genera factura          
                if limite_alcanzado == True:
                    print('\n¡ATENCIÓN! Ha comprado la cantidad máxima de productos,')
                    print('generando factura...\n')
                    print('*'*24,'FACTURA GENERAL','*'*25)
                    print('\nTotal Lays: ₡', total_lays)
                    print('Total huevos: ₡', total_huevos)
                    print("\nTotal bruto: ₡",total_bruto,'\n')
                    print('*'*66 + '\n')
                    mostrar_menu = False
                    agregar_nuevo = False

                # si no se alcanza límite, se pregunta si quiere comprar otro producto
                else:
                    print('\n'+'-'*66)
                    print("\nTotal hasta el momento: ₡",total_huevos or total_lays)
                    print('\n'+'-'*66)
                
                while agregar_nuevo:
                    print('\n¿Desea agregar un nuevo producto?\n\n[1] - Sí\n[2] - No\n')
                    continuar = input('Digite la opción de su preferencia: ')

                    if continuar == '1':
                        print('\nCONTINUANDO COMPRA...')
                        agregar_nuevo = False

                    elif continuar == '2':
                        print('\nCerrando menú de productos y generando factura...\n')
                        print('*'*24,'FACTURA GENERAL','*'*25)
                        print('\nTotal Lays: ₡', total_lays)
                        print('Total huevos: ₡', total_huevos)
                        print("\nTotal bruto: ₡",total_bruto,'\n')
                        print('*'*66 + '\n')
                        mostrar_menu = False
                        agregar_nuevo = False

                    else:
                        print('\n'+'-'*66 + '\n')
                        print('¡ERROR! Digite una opción válida!')
                        print('\n'+'-'*66+'\n')

            else:
                print('\n¡ERROR!, Por favor digite una opción de producto válida.')

    elif eleccion == '2':
        
        print('\nGracias por comprar en nuestra tienda\n')
        loop = False
    
    else:
        print('\nPor favor, ingrese una opción válida\n')
