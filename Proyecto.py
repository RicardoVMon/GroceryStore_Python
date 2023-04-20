# Validar nombre, día, mes, año y la cantidad que desea comprar
def validarNombre():

    preguntar_nombre = True
    while preguntar_nombre:
        nombre_cliente = input('\nPor favor, ingrese su nombre: ')
        if nombre_cliente == "":
            print('\n'+'-'*66 + '\n')
            print('¡ERROR! El nombre no puede estar vacío')
            print('\n'+'-'*66)
        else:
            preguntar_nombre = False
    
    return nombre_cliente
def validarDia():
    preguntar_dia = True
    while preguntar_dia:
        dia_compra = int(input('\nPor favor, ingrese el número de DÍA de su compra (1-31): '))
        if not 1 <= dia_compra <= 31 :
            print('\n'+'-'*66 + '\n')
            print('¡ERROR! Ingrese un valor de día válido')
            print('\n'+'-'*66)
        else:
            preguntar_dia = False
    
    return dia_compra
def validarMes():
    preguntar_mes = True
    while preguntar_mes:
        mes_compra = int(input('\nPor favor, ingrese el número de MES de su compra (1-12): '))
        if not 1 <= mes_compra <= 12:
            print('\n'+'-'*66 + '\n')
            print('¡ERROR! Ingrese un valor de mes válido')
            print('\n'+'-'*66)
        else:
            preguntar_mes = False
    
    return mes_compra
def validarAnnio():
    preguntar_annio = True
    while preguntar_annio:
        annio_compra = int(input('\nPor favor, ingrese el AÑO de su compra (Mayor a 2022): '))
        if annio_compra < 2023:
            print('\n'+'-'*66 + '\n')
            print('¡ERROR! El año debe ser mayor a 2022')
            print('\n'+'-'*66)
        else:
            preguntar_annio = False
    return annio_compra
def validarCantidadComprada():
    loop = True
    while loop:
        cantidad_producto = int(input('\nDigite la cantidad que desea comprar de ese producto: '))
        if cantidad_producto == 0 or cantidad_producto < 0:
            print('\n'+'-'*66 + '\n')
            print('ERROR, Debe comprar al menos 1 producto')
            print('\n'+'-'*66)
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
    
    loop = True
    while loop:
        print('¿Desea CONFIRMAR su compra?\n[1] - Sí\n[2] - No\n')
        eleccion = input('Ingrese la opción de su preferencia: ')
        if eleccion == '1':
            print('\n'+'-'*66)
            print('\nGuardando factura y volviendo al menú principal')
            print('\n'+'-'*66)
            guardarFactura()
            loop = False
        elif eleccion == '2':
            print('\n'+'-'*66)
            print('\nVolviendo al menú principal sin guardar factura')
            print('\n'+'-'*66)
            loop = False
        else:
            print('\n'+'-'*66 + '\n')
            print('ERROR, Ingrese una opción válida')
            print('\n'+'-'*66 + '\n')

def generarFactura():
    print('*'*24,'FACTURA GENERAL','*'*25)
    print('\n'+ '-'*24 +'DATOS DE LA COMPRA'+ '-'*24 +'\n')
    print('Nombre de cliente: ', nombre_cliente)
    print('Fecha: ' + str(dia_compra) + '/' + str(mes_compra) + '/' + str(annio_compra))
    
    # Loop que imprime todos los productos que tengan un monto acumulado en arreglo de productos
    print('\n'+ '-'*23 +'PRODUCTOS COMPRADOS'+ '-'*24 +'\n')
    for n in range(0,25):
        if matriz_productos[n][2] != 0:
            print(matriz_productos[n][0] + ':')
            print('Costo unitario: ₡' + str(matriz_productos[n][1]))
            print('Cantidad comprada: ' + str(matriz_productos[n][3]))
            print('Subtotal de ' + matriz_productos[n][0] + ': ₡' + str(matriz_productos[n][2]))
            print('\n')

    print('-'*23 +'INFORMACIÓN DE COSTOS'+ '-'*22 +'\n')
    print('Total bruto (Sin IVA): ₡', total_bruto)
    print('IVA (13%): ₡', calculo_iva)
    print('Descuento(Según cantidad comprada): ₡', monto_descuento)
    print('Total neto: ₡', total_neto)
    print('\n'+'*'*66 + '\n')

def guardarFactura():

    archivo = open('compras.txt', 'a')

    archivo.write('\n\n'+'*'*24 + 'FACTURA GENERAL' + '*'*25)
    archivo.write('\n')
    archivo.write('\n'+ '-'*24 +'DATOS DE LA COMPRA'+ '-'*24 +'\n\n')
    archivo.write('Nombre de cliente: ' + str(nombre_cliente) + '\n')
    archivo.write('Fecha: ' + str(dia_compra) + '/' + str(mes_compra) + '/' + str(annio_compra) + '\n')

    archivo.write('\n'+ '-'*23 +'PRODUCTOS COMPRADOS'+ '-'*24 +'\n\n')
    for n in range(0,25):
        if matriz_productos[n][2] != 0:
            archivo.write(matriz_productos[n][0] + ':')
            archivo.write('Costo unitario: ' + str(matriz_productos[n][1]) + '\n')
            archivo.write('Cantidad comprada: ' + str(matriz_productos[n][3])+ '\n')
            archivo.write('Subtotal de ' + matriz_productos[n][0] + ': ' + str(matriz_productos[n][2]) + '\n')
            archivo.write('\n')
    
    archivo.write('-'*23 +'INFORMACIÓN DE COSTOS'+ '-'*22 +'\n\n')
    archivo.write('Total bruto (Sin IVA): ' + str(total_bruto)+ '\n')
    archivo.write('IVA (13%): ' + str(calculo_iva)+ '\n')
    archivo.write('Descuento(Según cantidad comprada): ' + str(monto_descuento)+ '\n')
    archivo.write('Total neto: ' + str(total_neto)+ '\n')
    archivo.write('\n'+'*'*66 + '\n')

    archivo.close()

# ARREGLO DE PRODUCTOS (Nombre, Precio, Acumulado de cliente, Cantidad comprada)
matriz_productos = [['Arroz', 1200, 0, 0], #0
                    ['Frijoles', 2000 , 0, 0], #1
                    ['Lays', 600, 0, 0], #2
                    ['Huevos', 1500, 0, 0], #3
                    ['Leche', 1000, 0, 0], #4
                    ['Hersheys', 800, 0, 0], #5
                    ['Picaritas', 900, 0, 0], #6
                    ['Tronaditas', 700, 0, 0], #7
                    ['Atún', 2500, 0, 0], #8
                    ['Salmón', 3000, 0, 0], #9
                    ['Cremoleta', 1400, 0, 0], #10
                    ['Sal', 300, 0, 0], #11
                    ['Pimienta', 200, 0, 0], #12
                    ['Chirulitos', 750, 0, 0], #13
                    ['Mantequilla', 875, 0, 0], #14
                    ['Mayonesa', 450, 0, 0], #15
                    ['Tomate', 550, 0, 0], #16
                    ['Lechuga', 220, 0, 0], #17
                    ['Banano', 180, 0, 0], #18
                    ['Cebolla', 780, 0, 0], #19
                    ['Brócoli', 2200, 0, 0], #20
                    ['Jamón', 1625, 0, 0], #21
                    ['Zanahoria', 920, 0, 0], #22
                    ['Elote', 1050, 0, 0], #23
                    ['Limones', 715, 0, 0]] #24

# ARREGLO DE CEROS
productos_escogidos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Bienvenida
print('\nBienvenido a la tienda "Los Pollitos"\n')

# Loop principal
loop = True
while loop:
    
    # variables de totales en 0
    total_bruto = 0
    resetearEscogidos(productos_escogidos)
    resetearAcumulados(matriz_productos)
    limite_alcanzado = False
    
    print('1) Ingresar nueva compra\n2) Salir')
    eleccion = input('\nSeleccione la opción de su preferencia: ')

    if eleccion == '1':
        
        # Ciclo para validar nombre
        nombre_cliente = validarNombre()
        
        # Ciclo para validar que día sea menor a 31
        dia_compra = validarDia()

        # Ciclo para validar que meses no sean mayores a 12
        mes_compra = validarMes()
        
        # Ciclo para validar que año sea mayor a 2022
        annio_compra = validarAnnio()

        # Mostrar menú de compra
        mostrar_menu = True
        while mostrar_menu:  
            
            agregar_nuevo = True

            # Itera sobre arreglo de productos para imprimir nombre y precio
            print('\n' + '*'*24+' MENÚ DE PRODUCTOS '+ '*'*24 + '\n')
            for n in range(0,25):
                print('[' + str(n + 1) + ']-' + matriz_productos[n][0] + ': ₡' + str(matriz_productos[n][1]) )
            
            # Preguntar el número de objeto que desea
            numero_producto = int(input('\nDigite el número de producto que desea comprar: '))
            
            # Validar que el número de producto exista
            if numero_producto - 1 in range(0,25): 
                
                # Preguntar cantidad
                cantidad_producto = validarCantidadComprada()

                # Calcula el precio multiplicando cantidad por precio (Busca precio en arreglo de productos)
                calculo = matriz_productos[numero_producto - 1][1] * cantidad_producto

                # Agrega la cantidad comprada de el producto al arreglo
                matriz_productos[numero_producto - 1][3] = cantidad_producto
                
                # Agrega el monto de 'calculo' a arreglo de productos en acumulado de cliente
                matriz_productos[numero_producto - 1][2] += calculo
                
                # Agrega un '1' en arreglo de ceros, en la posición que indica usuario en 'numero_producto' 
                productos_escogidos[numero_producto - 1] = 1
                
                # Itera sobre arreglo de ceros sumando para saber si se alcanza límite, si sí, devuelve TRUE
                limite_alcanzado = cantidadMaxima(productos_escogidos)            

                # Si validación anterior es TRUE, o sea, alcanza límite, pasa esto.         
                if limite_alcanzado == True:
                    print('\n¡ATENCIÓN! Ha comprado la cantidad máxima de productos,')
                    print('generando factura...\n')
                    generarFactura()
                    finalizarCompra()

                    mostrar_menu = False
                    agregar_nuevo = False

                # Si no se alcanza límite, se realizan calculos de total bruto,
                # descuento, IVA y total neto para continuar comprando
                else:
                    
                    total_bruto = totalBruto(matriz_productos)
                    monto_descuento = descuentoCompra(productos_escogidos, total_bruto)
                    calculo_iva = total_bruto * 0.13
                    total_neto = total_bruto + calculo_iva - monto_descuento
                    print('\n'+'-'*66)
                    print("\nTotal hasta el momento: ₡",total_bruto)
                    print('\n'+'-'*66)
                
                # Se pregunta si desea agregar otro producto
                while agregar_nuevo:
                    print('\n¿Desea agregar un nuevo producto?\n\n[1] - Sí\n[2] - No\n')
                    continuar = input('Digite la opción de su preferencia: ')

                    # Si sí, continua comprando
                    if continuar == '1':
                        print('\nCONTINUANDO COMPRA...')
                        agregar_nuevo = False

                    # Si no, se despliega factura
                    elif continuar == '2':
                        print('\nCerrando menú de productos y generando factura...\n')
                        generarFactura()
                        finalizarCompra()

                        mostrar_menu = False
                        agregar_nuevo = False

                    else:
                        print('\n'+'-'*66 + '\n')
                        print('¡ERROR! Digite una opción válida!')
                        print('\n'+'-'*66)

            else:
                print('\n'+'-'*66 + '\n')
                print('¡ERROR!, Por favor digite una opción de producto válida.')
                print('\n'+'-'*66)

    elif eleccion == '2':
        
        print('\nGracias por comprar en nuestra tienda\n')
        loop = False
    
    else:
        print('\n'+'-'*66 + '\n')
        print('¡ERROR!, Por favor ingrese una opción válida')
        print('\n'+'-'*66 + '\n')