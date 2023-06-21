import json
import csv
import random

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
    print("|10-Mostrar stock por marca         |")
    print("|11-Generar lista bajo stock        |")
    print("|12-Agregar nuevo produto           |")
    print("|13-Guarda en formato csv o json    |")
    print("|14-Salir del programa              |")
    print("|___________________________________|")
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            input("Error. Ingrese una opcion valida!")
    return opcion


# 1:
import csv

def cargar_datos_desde_csv():
    insumos = []  # lista para almacenar

    while True:
        nombre_archivo = str(input("Ingrese el nombre del archivo: "))
        nombre_archivo = nombre_archivo.strip() + ".csv"
        if nombre_archivo:
            try:
                with open(nombre_archivo, "r", encoding='utf-8') as archivo:
                    next(archivo)
                    datos = archivo.readlines()
                    datos = [line.strip().split(",") for line in datos]

                    for linea in datos:
                        insumo = calcular_stock(linea)
                        insumos.append(insumo)

                    break
            
            except FileNotFoundError:
                print("El archivo no existe. Ingrese un nombre valido!")
        else:
            print("Debe ingresar un nombre de archivo!")
    
    return insumos


def calcular_stock(datos):
    insumo = {
        'id': int(datos[0]),
        'nombre': datos[1],
        'marca': datos[2],
        'precio': float(datos[3].replace('$', '')),
        'caracteristicas': datos[4].split("~"),
        'stock': random.randint(0, 10)
    }  
    return insumo



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

    marcas = {}  #diccionario para almacenar
    
    for insumo in lista:
        marca = insumo['marca']
        nombre = insumo['nombre']
        precio = insumo['precio']

        if marca in marcas:
            #si la marca ya existe en el diccionario, agrega el insumo y el precio
            marcas[marca].append((nombre, precio))
        else:
            marcas[marca] = [(nombre, precio)]

    print(" _______________________________________________________________________________")
    print("|                         Listado de marcas e insumos                           |")
    print("|_______________________________________________________________________________|")
    print("|                MARCA                   |             NOMBRE            |PRECIO|")
    print("|_______________________________________________________________________________|")

    for marca in marcas:  #recorro las marcas
        first = True  #flag para indicar si es la primera vez que se muestra la marca
        for nombre, precio in marcas[marca]:  # recorro los items
            if first:
                print("|-------------------------------------------------------------------------------|")
                print(f"|{marca:40}|{nombre:31}|{precio:5.2f} |")
                first = False
            else:
                print(f"|{' ':40}|{nombre:31}|{precio:5.2f} |")
                #print("|-------------------------------------------------------------------------------|")
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
    print("|    ID   |          Nombre           |   Precio   |   stock  |")
    print("|-------------------------------------------------------------|")
    for producto in lista:
        if producto['marca'] == marca:
            print(f"| {producto['id']:6} | {producto['nombre']:25} |  {producto['precio']:.2f}  |  {producto['stock']:2}  |")
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
        print("|    ID   |          Nombre           |      Precio      |      Stock      |")
        for insumo in insumos_por_marca:
            print(
                f"|Id: {insumo['id']:2} | Nombre: {insumo['nombre']:20} | Precio: {insumo['precio']:.2f} |   {insumo['stock']:2} |")
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
        
    seguir_comprando = True

    while seguir_comprando:
        marca_ingresada = str(input("Ingresa la marca deseada ('q' para salir): ")).capitalize()
        if marca_ingresada.lower() == "q":
            break

        productos_marcas = []
        for producto in lista:
            if producto["marca"] == marca_ingresada:
                productos_marcas.append(producto)
        
        if not productos_marcas:
            print(f"No se encontro la marca '{marca_ingresada}' en la lista de productos!")
            continue

        flag_insumo = True
        producto_seleccionado = None
        while flag_insumo:
            listar_insumo_por_marca(lista, marca_ingresada)
            try:
                insumo = int(input("Ingrese ID del producto: "))
            except ValueError:
                    print("No puede ingresar un ID en blanco!")
                    insumo = ''
            else:
                for producto in productos_marcas:
                        if producto["id"] == insumo:
                            producto_seleccionado = producto
                            break
            
            if producto_seleccionado is None:
                print(f"No se encontro el ID: {insumo} en la marca '{marca_ingresada}'!")
                continue

            producto_encontrado = producto_seleccionado["nombre"]
            precio = producto_seleccionado["precio"]
            stock = producto_seleccionado["stock"]

            try:
                cantidad = int(input("Ingrese la cantidad a comprar: "))
            except ValueError:
                    print("No puede ingresar cantidad en blanco!")
                    cantidad = ''
            else:
                if cantidad is None or cantidad <= 0:
                    print("Error: la cantidad debe ser un numero entero positivo!")
                    continue
            
            if cantidad > stock:
                print(f"No hay suficiente stock disponible. Stock actual: {stock}")
                try:
                    respuesta = input("Desea comprar una cantidad menor? (s/n): ")
                except ValueError:
                    print("Ingrese solo (s/n)!")
                    respuesta = ''
                else:
                    if respuesta.lower() != 's':
                        continue
                cantidad = stock #se baja automaticamente a la cantidad de stock que haya
            
            subtotal = calcular_subtotal(cantidad, precio)
            total += subtotal
            compra.append((producto_encontrado, cantidad, precio, float(subtotal)))

            print("Compra agregada al carrito!")

            respuesta = input("Desea agregar otro producto de esta marca? (s/n): ")
            if respuesta.lower() != 's':
                flag_insumo = False
            
        respuesta = input("Desea seguir comprando?(s/n): ")
        if respuesta.lower() != 's':
            generar_factura(compra, total)
            seguir_comprando = False


def calcular_subtotal(cantidad, precio):
    return cantidad * precio


def generar_factura(compra, total):
    
    nombre_archivo = str(input("Ingrese el nombre de la factura: "))
    nombre_archivo = nombre_archivo.strip() + ".txt"

    factura = "Factura de la compra:\n\n"
    subtotal = 0

    for item in compra:
        producto, cantidad, precio, subtotal_item = item #utilizo el metodo de desempaquetado que encontre en google https://j2logo.com/python/tutorial/tipo-tuple-python/
        subtotal += subtotal_item
        factura += f"{producto} - Cantidad: {cantidad} - Precio: ${precio} - Subtotal: ${subtotal_item:.2f}\n" #concateno las cadenas
    
    factura += f"total de compra: ${total}"

    with open(nombre_archivo,"w") as archivo:
        archivo.write(factura)




#7
def guardar_en_formato_json(lista):

    productos_filtrados = list(filter(lambda producto: "Alimento" in producto["nombre"], lista))

    with open("productos_alimentos.json", "w") as archivo:
        json.dump(productos_filtrados, archivo, indent=4)

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

    with open("insumos.csv", "w", encoding="utf=8") as archivo:
        archivo.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")

        for item in productos_actualizados:
            caracteristicas = "~".join(item['caracteristicas'])
            linea = "{},{},{},${},{}\n".format(item['id'], item['nombre'], item['marca'], item['precio'], caracteristicas)
            
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

    max_id = 0
    for item in lista:
        if item["id"] > max_id:
            max_id = item["id"]
    
    nuevo_insumo["id"] = max_id + 1


    #pido el insumo
    while True:
        try:
            nombre_insumo = str(input("Ingrese nombre del producto: "))
            if not nombre_insumo:
                print("El nombre del producto no puede estar vacio!")
            else:
                nuevo_insumo["nombre"] = nombre_insumo
                break
        except ValueError:
            print("Error! Reingrese nombre.")

    #pido la marca
    mostrar_marcas(marcas)
    while True:
        try:
            marca_indice = int(input("Ingrese el numero de la marca que quiera agregar: "))
        except ValueError:
            print("Error! Reingrese marca.")
        else:
            if marca_indice <= 0 or marca_indice >= len(marcas):
                print("El numero de marca ingresado no es valido!")
            nuevo_insumo["marca"] = marcas[marca_indice]
            break

    #pido el precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Error! Reingrese precio.")
        else:
            if precio <= 0:
                print("El precio debe ser mayor a 0!")
            else:
                nuevo_insumo['precio'] = precio
                break

    #pido las caracteristicas
    caracteristicas = []
    while True:
        try:
            cantidad_caracteristica = int(input("Ingrese el numero de caracteristicas a agregar (1/3): "))
        except ValueError:
            print("Error: Ingrese un numero valido!")
        else:
            if(cantidad_caracteristica < 1 or cantidad_caracteristica > 3):
                print("El minimo de caracteristicas es 1 y el maximo 3!")
            else:
                cantidad_caracteristica = max(1, min(cantidad_caracteristica, 3))
                break

    for item in range(cantidad_caracteristica):
        while True:
            try:
                caracteristica = str(input(f"Ingrese la caracteristica {item + 1}: ")).capitalize()
            except ValueError:
                print("Error! Reingrese caracteristica.")
            else:
                if not caracteristica:
                    print("Ingreso una caracteristica vacia!")
                caracteristicas.append(caracteristica)
                break

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


#recuperatorio

#D
def mostrar_stock_por_marca(lista):
    
    pedir_marca = True
    
    listar_cantidad_por_marca(lista)
    
    while pedir_marca:
        marca_ingresada = str(input("Ingresa la marca deseada ('q' para salir): ")).capitalize()

        for producto in lista:
            if producto["marca"] == marca_ingresada:
                pedir_marca = False
                break
        
        if pedir_marca:
            print(f"No se encontro la marca: {marca_ingresada}")


    stock_total = 0
    for producto in lista:
        if producto['marca'] == marca_ingresada:
            stock_total += producto["stock"]
    
    print("|---------------------------------------------------------|")
    print(f"|          lista de stock: '{marca_ingresada}'                        |")
    print("|---------------------------------------------------------|")
    print(f"|Stock total de la marca: {stock_total}                              |")
    print("|---------------------------------------------------------|")


#C
def imprimir_bajo_stock(lista):
    
    productos_bajo_stock = []
    for producto in lista:
        if producto.get("stock", 0) <= 2:
            productos_bajo_stock.append((producto["nombre"], producto["stock"]))

    if not productos_bajo_stock:
        print("No hay productos con 2 o menos unidades de stock.")

    while True:
        try:
            nombre_archivo = str(input("Ingrese nombre del archivo CSV a generar: "))
            if not nombre_archivo:
                raise ValueError
            else:
                nombre_archivo = nombre_archivo.strip() + ".csv"
                break
        except ValueError:
            print("No puede ingresar un nombre de archivo en blanco!")

    
    with open(nombre_archivo, "w", encoding="utf=8") as archivo_csv:
        archivo_csv.write("Nombre producto | Stock\n")
        for producto in productos_bajo_stock:
            archivo_csv.write(f"{producto[0]}, {producto[1]}\n")

    print(f"Archivo CSV generado!: {nombre_archivo}")