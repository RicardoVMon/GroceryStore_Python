# Validar nombre, día, mes, año y la cantidad que desea comprar
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
    return annio_compra
def validarCantidadComprada():
    loop = True
    while loop:
        cantidad_producto = int(input('\nDigite la cantidad que desea comprar de ese producto: '))
        if cantidad_producto == 0 or cantidad_producto < 0:
            print('\nERROR, Debe comprar al menos 1 producto')
        else:
            return cantidad_producto    

# Itera sobre lista de 0s y suma los 1s para medir cantidad comprada
def cantidadMaxima(arreglo_de_ceros):
    sumatoria = 0
    for n in range(0,25):
        sumatoria += arreglo_de_ceros[n]

    if sumatoria == 20:
        return True

# Suma la posición de acumulado de cliente del arreglo para total bruto
def totalBruto(arreglo_de_productos):
    sumatoria = 0
    for n in range(0,25):
        sumatoria += arreglo_de_productos[n][2]
    return sumatoria

# Resetea la lista de 0s y los acumulados de cliente del arreglo
def resetearEscogidos(arreglo_de_ceros):
    for n in range(0,25):
        arreglo_de_ceros[n] = 0
    return arreglo_de_ceros
def resetearAcumulados(arreglo_de_productos):
    for n in range(0,25):
        arreglo_de_productos[n][2] = 0
    return arreglo_de_productos

# Mide la cantidad de 1s en el arreglo de ceros y calcula porcentaje según eso sobre el total bruto
def descuentoCompra(arreglo_de_ceros, total_bruto):
    sumatoria = 0
    for n in range(0,25):
        sumatoria += arreglo_de_ceros[n]
    
    if 0 < sumatoria <= 5:
        monto_descuento = total_bruto * 0.02
    elif  5 < sumatoria <= 10:
        monto_descuento = total_bruto * 0.05
    else:
        monto_descuento = total_bruto * 0.07
    
    return monto_descuento

# Pregunta si desea confirmar compra para guardar o no la factura
def finalizarCompra():
    print('¿Desea CONFIRMAR su compra?\n[1] - Sí\n[2] - No\n')
    eleccion = input('Ingrese la opción de su preferencia: ')
    if eleccion == '1':
        print('\n'+'-'*66)
        print('\nGuardando factura y volviendo al menú principal')
        print('\n'+'-'*66)
    elif eleccion == '2':
        print('\n'+'-'*66)
        print('\nVolviendo al menú principal sin guardar factura')
        print('\n'+'-'*66)
    else:
        print('\nERROR, Ingrese una opción válida\n')

# ARREGLO DE PRODUCTOS (Nombre, Precio, Acumulado de cliente)
productos_tienda = [['Arroz', 1200, 0], #0
                    ['Frijoles', 2000 , 0], #1
                    ['Lays', 600, 0], #2
                    ['Huevos', 1500, 0], #3
                    ['Leche', 1000, 0], #4
                    ['Hersheys', 800, 0], #5
                    ['Picaritas', 900, 0], #6
                    ['Tronaditas', 700, 0], #7
                    ['Atún', 2500, 0], #8
                    ['Salmón', 3000, 0], #9
                    ['Cremoleta', 1400, 0], #10
                    ['Sal', 300, 0], #11
                    ['Pimienta', 200, 0], #12
                    ['Chirulitos', 750, 0], #13
                    ['Mantequilla', 875, 0], #14
                    ['Mayonesa', 450, 0], #15
                    ['Tomate', 550, 0], #16
                    ['Lechuga', 220, 0], #17
                    ['Banano', 180, 0], #18
                    ['Cebolla', 780, 0], #19
                    ['Brócoli', 2200, 0], #20
                    ['Jamón', 1625, 0], #21
                    ['Zanahoria', 920, 0], #22
                    ['Elote', 1050, 0], #23
                    ['Limones', 715, 0]] #24

# ARREGLO DE CEROS
productos_escogidos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
