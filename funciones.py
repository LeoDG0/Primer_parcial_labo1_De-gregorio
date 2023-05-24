import json

def menuPrincipal():
    print(" ___________________________________")
    print("|                                   |")
    print("|  ***Administracion de insumos***  |")
    print("|___________________________________|")
    print("|1-Cargar dato                      |")
    print("|2-Listar cantidad por marca        |")
    print("|3-Listar insumos por marca         |")
    print("|4-Buscar insumo por caracteristica |")
    print("|5-Listar insumos ordenados         |")
    print("|6-Realizar compras                 |")
    print("|7-Guardar en formato JSON          |")
    print("|8-Leer desde formato JSON          |")
    print("|9-Actualizar precios               |")
    print("|10-Agregar nuevo produto           |")
    print("|11-Guarda en formato csv o json    |")
    print("|12-Salir del programa              |")
    print("|___________________________________|")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            input("Error. Ingrese una opcion valida!")
    return opcion


# 1:
def cargar_datos_desde_csv():

    insumos = []  # lista para almacenar

    with open("insumos.csv", "r", encoding='utf-8') as archivo:
        next(archivo)

        for linea in archivo:
            # saca los espacios en blanco y separa por campos en base a la ,
            linea = linea.strip("\n").split(',')

            insumo = {
                'id': int(linea[0]),
                'nombre': linea[1],
                'marca': linea[2],
                'precio': float(linea[3].replace('$', '')),
                'caracteristicas': linea[4].split("~")
            }  # obtengo los datos

            insumos.append(insumo)  # agrego el diccionario a la lista

    return insumos


# 2:
def listar_cantidad_por_marca(lista):

    cantidad_por_marca = {}

    for insumo in lista:
        marca = insumo['marca']
        if marca in cantidad_por_marca:
            cantidad_por_marca[marca] += 1  # sumo si ya esta
        else:
            cantidad_por_marca[marca] = 1  # inicio en 1 si no esta

    print(" _____________________________________________________")
    print("|                  Listado de marcas                  |")
    print("|_____________________________________________________|")
    for marca in cantidad_por_marca:
        cantidad = cantidad_por_marca[marca]
        print(f"|Marca: {marca:25} | Cantidad: {cantidad}       |")
        print("|_____________________________________________________|")


# 3:
def listar_insumos_por_marca(lista):

    marcas = {}  # diccionario para almacenar

    for insumo in lista:
        marca = insumo['marca']
        nombre = insumo['nombre']
        precio = insumo['precio']

        if marca in marcas:
            # si esta la marca en la lista agrega el insumo y el precio #uso tuplas para almacenar cada insumo
            marcas[marca].append((nombre, precio))
        else:
            # si no esta la marca la crea y agrega el insumo y el precio
            marcas[marca] = [(nombre, precio)]

    print(" _______________________________________________________________________________")
    print("|                         Listado de marcas e insumos                           |")
    print("|_______________________________________________________________________________|")
    print("|                MARCA                   |             NOMBRE            |PRECIO|")
    print("|_______________________________________________________________________________|")
    for marca in marcas:  # recorro las marcas
        for nombre, precio in marcas[marca]:  # recorro los items
            print(f"|{marca:40}|{nombre:31}|{precio:5.2f} |")
            print(
                "|-------------------------------------------------------------------------------|")
    print("|_______________________________________________________________________________|")


# 4:
def validar_string_input():

    while True:
        mensaje = input("Ingrese: ")
        if (mensaje.replace(" ", "").isalnum()):  # no se me ocurrio una forma de validar que sea letras y que cuente los espacios en blanco asi que busque en google una funcion que tome los espacios en blanco
            break  # https://www.programiz.com/python-programming/methods/string/isalnum
        else:
            print("Error: Debe ingresar un valor valido!(letras y espacios)")

    return mensaje


def buscar_insumo_por_caracteristica(lista):

    # valido que sea solo letras y espacio en blanco
    caracteristica = validar_string_input()

    insumos_por_caracteristica = []  # lista para guardar los insumos

    for insumo in lista:
        # capitalizo caracteristica para que no importe si se agrega una minuscula o mayuscula
        if caracteristica.capitalize() in insumo['caracteristicas']:
            insumos_por_caracteristica.append(insumo)

    if (len(insumos_por_caracteristica) > 0):  # pregunto si se encontraron insumos
        print(
            " ____________________________________________________________________________")
        print(
            f"|   Insumos con la caracteristica: {caracteristica.capitalize():20}                      |")
        print(
            "|____________________________________________________________________________|")
        for insumo in insumos_por_caracteristica:
            print(
                f"|Id: {insumo['id']:2} | Nombre: {insumo['nombre']:20} | Marca: {insumo['marca']:29}|")
            print(
                "|----------------------------------------------------------------------------|")
        print(
            "|____________________________________________________________________________|")
    else:
        print(
            f"No se encontraron insumos con la caracteristica {caracteristica}")


# 5:
def listar_insumos_ordenados(lista):

    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            # ordena las marcas de alfabeticamente y si son iguales las ordena por precio decendente
            if (lista[i]['marca'] > lista[j]['marca'] or lista[i]['marca'] == lista[j]['marca'] and lista[i]['precio'] < lista[j]['precio']):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    print(" ____________________________________________________________________________________________________________________________________________________________________________")
    print("|                                                                     *** lista de insumos ***                                                                               |")
    print("|____________________________________________________________________________________________________________________________________________________________________________|")
    print("|ID |               NOMBRE                |             MARCA              | PRECIO |                                    CARACTERISTICAS                                     |")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    for insumo in lista:
        id = insumo['id']
        nombre = insumo['nombre']
        marca = insumo['marca']
        precio = insumo['precio']
        caracteristicas = insumo['caracteristicas'][0]  # primer caracteristica

        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(
            f"|{id:2} | {nombre:35} | {marca:30} | ${precio:5.2f} | {caracteristicas:87}|")
    print("|____________________________________________________________________________________________________________________________________________________________________________|")


# 6:
def validar_int_input():

    while True:
        try:
            mensaje = int(input("Ingrese: "))
            break
        except ValueError:
            print("Error: debe ingresar un id valido(solo numero/s)!")

    return mensaje



def listar_productos_por_marca(lista, marca):
    print(f"Insumos de la marca: {marca}")
    print("_______________________________________________________________")
    print("|    ID   |          Nombre           |   Precio   |")
    print("|-------------------------------------------------------------|")
    for producto in lista:
        if producto['marca'] == marca:
            print(f"| {producto['id']:6} | {producto['nombre']:25} | {producto['precio']:.2f} |")
    print("|_____________________________________________________________|")



def listar_insumo_por_marca(lista, marca):

    insumos_por_marca = []  # lista para guardar los insumos

    for insumo in lista:
        if marca.capitalize() in insumo['marca']:
            insumos_por_marca.append(insumo)

    if (len(insumos_por_marca) > 0):  # pregunto si se encontraron insumos
        print(
            " ____________________________________________________________________________")
        print(
            f"|      Insumos de la marca: {marca.capitalize():20}                         |")
        print(
            "|____________________________________________________________________________|")
        for insumo in insumos_por_marca:
            print(
                f"|Id: {insumo['id']:2} | Nombre: {insumo['nombre']:20} | Precio: {insumo['precio']:6}|")
            print(
                "|----------------------------------------------------------------------------|")
        print(
            "|____________________________________________________________________________|")
    else:
        print(f"No se encontraron insumos con la caracteristica {marca}")




def realizar_compras(lista):
    compra = [] #inicializo las variables
    total = 0
    
    listar_cantidad_por_marca(lista)
        
    flag_marca = True
    salir = 's'
    flag_calculos = False
    flag_producto = False
    seguir_comprando = True #inicializo las flags

    while seguir_comprando: #se encarga de verificar si la marca que se ingreso existe
        
        while flag_marca:
            marca_ingresada = str(input("Ingrese marca deseada('q' para salir): ")).capitalize()
            if(marca_ingresada.lower() == 'q'):
                salir = 's'
                break
            else:
                for item in lista:
                    if marca_ingresada.capitalize() == item['marca']:
                        flag_insumo = True
                        flag_marca = False

            while flag_insumo: #verifica que el ID que se ingreso existe y agrega los valores
                salir_insumos = 'n'
                for producto in lista:
                    if(marca_ingresada == producto['marca']):
                        listar_insumo_por_marca(lista, marca_ingresada)
                        insumo = int(input("Ingrese el ID del producto: "))
                        if (producto['id'] == insumo):
                            producto_encontrado = producto['nombre']
                            precio = producto['precio']
                            flag_producto = True
                            flag_calculos = True  #mediante las flags activo y desactivo los bucles while cambiando el valor de las flags

                        if(flag_producto == False):
                            print(f"Error: No se encontro el ID: {insumo}!")
                            break
                        
                        print("Ingresa la cantidad a comprar: ")
                        cantidad = validar_int_input()

                        salir_insumos = str(input("Desea agregar otro insumo de esta marca?(s/n)"))
                        if(salir_insumos.lower() == 'n'):
                            flag_insumo = False
                            break

                if(flag_calculos == True):
                    if(cantidad > 0 and precio > 0):
                        
                        subtotal = calcular_subtotal(cantidad, precio)
                        total += subtotal
                        compra.append((producto_encontrado, cantidad, precio, float(subtotal))) #hago todo los calculos y los agrego a la lista de compra en tuplas

                        print("Compra agregada al carrito!")
                    else:
                        print("Ocurrio un error!")
                        continue
        
        salir = str(input("Desea seguir comprando?(s/n): "))
        if(salir == "s"):
            flag_marca = True
        elif(salir == 'n'):
            generar_factura(compra, total) #llamo a la funcion que genera el txt y le paso la lista de compra y el total
            seguir_comprando = False
            break


def calcular_subtotal(cantidad, precio):
    return cantidad * precio


def generar_factura(compra, total):
    factura = "Factura de la compra:\n\n"
    subtotal = 0

    for item in compra:
        producto, cantidad, precio, subtotal_item = item #utilizo el metodo de desempaquetado que encontre en google https://j2logo.com/python/tutorial/tipo-tuple-python/
        subtotal += subtotal_item
        factura += f"{producto} - Cantidad: {cantidad} - Precio: ${precio} - Subtotal: ${subtotal_item:.2f}\n" #concateno las cadenas
    
    factura += f"total de compra: ${total}"

    with open("factura.txt","w") as archivo:
        archivo.write(factura)




#7
def guardar_en_formato_json(lista):

    productos_filtrados = list(filter(lambda producto: "Alimento" in producto["nombre"], lista))

    with open("productos_alimentos.json", "w") as archivo:
        json.dump(productos_filtrados, archivo, indent=4, separators=(", "))

    print("Archivo JSON generado!")


#8

def leer_archivo_json():
    
    with open ("productos_alimentos.json", "r") as archivo:
        productos = json.load(archivo)

    print(" ____________________________________________________________________________________________________________________________________________________________________________")
    print("|                                                                     *** lista de insumos de alimentos ***                                                                  |")
    print("|____________________________________________________________________________________________________________________________________________________________________________|")
    print("|ID |               NOMBRE                |             MARCA              | PRECIO |                                    CARACTERISTICAS                                     |")
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    for insumo in productos:
        id = insumo['id']
        nombre = insumo['nombre']
        marca = insumo['marca']
        precio = insumo['precio']
        print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f"|{id:2} | {nombre:35} | {marca:30} | ${precio:5.2f} | {'':87}|")
        for caracteristicas in insumo['caracteristicas']:
            print(f"|{'':2} | {'':35} | {'':30} |  {'':5} | {caracteristicas:87}|")
    print("|____________________________________________________________________________________________________________________________________________________________________________|")

#9

def aplicar_aumento(lista):
    lista['precio'] *= 1.084
    return lista

def actualizar_precios(lista):
    
    productos_actualizados = list(map(aplicar_aumento,lista))

    with open("insumos.csv", "w") as archivo:
        archivo.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")

        for item in productos_actualizados:
            linea = f"{item['id'],item['nombre'],item['marca'],item['precio'],item['caracteristicas']}\n"

            archivo.write(linea)

    print("Los precios se actualizaron correctamente!")


#2da parte parcial:

#1
def cargar_marcas():
    with open("marcas.txt", "r") as archivo:
        marcas = archivo.read().splitlines()
    
    return marcas

def guardar_marcas(marcas):
    with open("marcas.txt", "w") as archivo:
        for marca in marcas:
            archivo.write(marca + "\n")

def mostrar_marcas(marcas):
    print(" _____________________________")
    print("|                             |")
    print("|     Marcas disponibles      |")
    for i in range(len(marcas)):
        print("|-------------------------|")
        print(f"|{i} | {marcas[i]:5}|")
        print("|_________________________|")


def agregar_productos(lista, marcas):

    nuevo_insumo = {}

    #pido el id 
    while True:
        id_insumo_nuevo = int(input("Ingrese un ID para el producto: "))

        flag_id = False
        for item_id in lista:
            if(id_insumo_nuevo == item_id["id"]):
                flag_id = True
                
            
        if (flag_id):
            print("El ID ingresado ya existe. Intente con ID mayores a 50: ")
        else:
            nuevo_insumo["id"] = id_insumo_nuevo
            break


    #pido el insumo
    nombre_insumo = str(input("Ingrese nombre del producto: "))
    nuevo_insumo["nombre"] = nombre_insumo

    #pido la marca
    mostrar_marcas(marcas)
    marca_indice = int(input("Ingrese el numero de la marca que quiera agregar: "))
    nuevo_insumo["marca"] = marcas[marca_indice]

    #pido el precio
    precio = float(input("Ingrese el precio del producto: "))
    nuevo_insumo['precio'] = precio


    #pido las caracteristicas
    caracteristicas = []
    cantidad_caracteristica = int(input("Ingrese el numero de caracteristicas a agregar (1/3): "))
    cantidad_caracteristica = max(1, min(cantidad_caracteristica, 3))

    for item in range(cantidad_caracteristica):
        caracteristica = str(input(f"Ingrese la caracteristica {item + 1}: "))
        caracteristicas.append(caracteristica)

    nuevo_insumo["caracteristicas"] = caracteristicas

    #agrego el insumo nuevo
    lista.append(nuevo_insumo)
    print("Producto agregado con exito!")


#2

def guardar_tipo_archivo(lista):

    formato = int(input("Ingrese el formato que desea (1: CSV | 2: JSON): "))

    if (formato == 1):
        nombre_archivo = str(input("Ingrese el nombre del archivo: "))
        nombre_archivo = nombre_archivo.strip() + ".csv"

        with open(nombre_archivo,"w", newline='', encoding="utf=8") as archivo:
            archivo.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")

            for item in lista:
                linea = f"{item['id'],item['nombre'],item['marca'],item['precio'],item['caracteristicas']}\n"
                archivo.write(linea)

        print("Datos guardados en formato CSV!")

    elif(formato == 2):
        nombre_archivo = str(input("Ingrese el nombre del archivo: "))
        nombre_archivo = nombre_archivo.strip() + ".json"

        with open(nombre_archivo, "w", encoding="utf=8") as archivo:
            json.dump(lista, archivo, indent=2)

        print("Datos guardados en formato JSON!")

    else:
        print("ERROR: Formato de archivo no valido!")




