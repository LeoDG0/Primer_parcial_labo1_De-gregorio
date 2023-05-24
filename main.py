""" 
Se solicita desarrollar un programa para administrar los insumos de una 
tienda de mascotas. Para ello, se dispone de un archivo CSV con el 
siguiente formato:

ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS
1,Alimento para perros,Pedigree,$12.99,Sabor delicioso~Nutrición 
equilibrada~Contiene vitaminas y minerales

El programa debe ofrecer un menú con las siguientes opciones:

1. Cargar datos desde archivo: Esta opción permite cargar el contenido del archivo "Insumos.csv" en una colección, teniendo en cuenta que 
las características de los insumos deben estar en un tipo de colección integrada.

2. Listar cantidad por marca: Muestra todas las marcas y la cantidad de insumos correspondientes a cada una.

3. Listar insumos por marca: Muestra, para cada marca, el nombre y precio de los insumos correspondientes.

4. Buscar insumo por característica: El usuario ingresa una característica (por ejemplo, "Sin Granos") y se listarán todos los 
insumos que poseen dicha característica

5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca y la primera característica de todos los productos, ordenados por 
marca de forma ascendente (A-Z) y, ante marcas iguales, por precio descendente.

6. Realizar compras: Permite realizar compras de productos. El usuario ingresa una marca y se muestran todos los productos disponibles de esa marca. 
Luego, el usuario elige un producto y la cantidad deseada. 
Esta acción se repite hasta que el usuario decida finalizar la compra. 
Al finalizar, se muestra el total de la compra y se genera un archivo 
TXT con la factura de la compra, incluyendo cantidad, producto, 
subtotal y el total de la compra.

7. Guardar en formato JSON: Genera un archivo JSON con todos los productos cuyo nombre contiene la palabra "Alimento".

8. Leer desde formato JSON: Permite mostrar un listado de los insumos guardados en el archivo JSON generado en la opción anterior.

9. Actualizar precios: Aplica un aumento del 8.4% a todos los productos, utilizando la función map. Los productos actualizados se guardan en el archivo "Insumos.csv".

10. Salir del programa

"""
import os
from funciones import *

lista = []
flag_datos = False
flag_json = False
flag_insumo_nuevo = False

while True:
    os.system("cls")
    match(menuPrincipal()):
        
        case 1:
            lista = cargar_datos_desde_csv()
            flag_datos = True
        case 2:
            if(flag_datos == True):
                listar_cantidad_por_marca(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 3:
            if(flag_datos == True):
                listar_insumos_por_marca(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 4:
            if(flag_datos == True):
                buscar_insumo_por_caracteristica(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 5:
            if(flag_datos == True):
                listar_insumos_ordenados(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 6:
            if(flag_datos == True):
                realizar_compras(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 7:
            if(flag_datos == True):
                guardar_en_formato_json(lista)
                flag_json = True
            else:
                print("Primero se deben cargar los datos!")
        case 8:
            if(flag_datos == True and flag_json == True):
                leer_archivo_json()
            else:
                print("Primero se deben cargar los datos y el archivo json!")
        case 9:
            if(flag_datos == True):
                actualizar_precios(lista)
            else:
                print("Primero se deben cargar los datos!")
        case 10:
            if(flag_datos == True):
                agregar_productos(lista, cargar_marcas())
                flag_insumo_nuevo = True
            else:
                print("Primero se deben cargar los datos!")
        case 11:
            if(flag_datos == True and flag_insumo_nuevo == True):
                guardar_tipo_archivo(lista)
            else:
                print("Primero se deben cargar los datos y agregar un producto!")
        case 12:
            salir = input("Confirma salida? (s/n)")
            if(salir.lower() == "s"):
                break
            elif(salir.lower() == "n"):
                print("cancelando salida!")
            else:
                print("Ingreso una opcion invalida!")
    os.system("pause")























