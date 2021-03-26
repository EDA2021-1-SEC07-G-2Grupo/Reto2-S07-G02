"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada

"""
def print_separador():
    print("-----------------------------------------------(￣(工)￣)--------------------------------------------")


def imprime_toda_lista_econtrada_req1(catalog):
    print(print_separador())
    n=0
    while n<lt.size(catalog):
            video_ordenado=lt.getElement(catalog,n)
            print("Posición: "+str(1+n))
            print("-"+"Trending_date: "+video_ordenado["trending_date"])
            print("-"+"Title: "+video_ordenado["title"])
            print("-"+"Chanel_title: "+video_ordenado["channel_title"])
            print("-"+"Publish_time: "+video_ordenado["publish_time"])
            print("-"+"Views: "+video_ordenado["views"])
            print("-"+"Likes: "+video_ordenado["likes"])
            print("-"+"Dislikes: "+video_ordenado["dislikes"])
            print(print_separador())
            n+=1

def print_req3(catalog):
    vid=lt.firstElement(catalog)
    print("-"+"Title: "+vid["title"])
    print("-"+"Channel title: "+vid["channel_title"])
    print("-"+"Category ID "+vid["category_id"])
    print("-"+"Días: "+str(vid["views"]))
   

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo") 
    print("2- Consultar n número de videos más vistos por país y en una categoría especifica")
    print("3- Consultar el video más trending por país(pais)")
    print("4- Consultar el video más trending por categoría (categoría)")
    print("5- Consultar los n videos con más likes por 'tag' de acuerdo a un país especifico")
    print("0- Salir")

    
def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')


    if int(inputs[0]) == 1:


        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print ("Videos Cargados "+str(controller.sizeLista(catalog["video"])))
        print ("Categorias cargadas "+str(controller.sizeMapas(catalog["category_id"])))


    elif int(inputs[0]) == 2:

        pei=str(input("Escriba el nombre del país que desea consultar \n"))
        if mp.contains(catalog["country"], pei)== False:
            print_separador()
            print("No se ha encontrado ningun video del país "+ str(pei))
            print_separador()
        else:
            videos_por_pais=(controller.Getalgobycatalogyllave(catalog["country"],pei))
            categ=str(input("Escriba el numero de la categoria de los videos que desea consultar \n"))
            if mp.contains(catalog["category_id"],str(categ))==False:
                print_separador()
                print("No se ha encontrado ninguna categoría "+ str (categ))
                print_separador()
            else:
                Vids_por_pais_categ=controller.Getvideosbycateg(videos_por_pais,categ)
                if lt.isEmpty(Vids_por_pais_categ)==True:
                    print(lt.size(Vids_por_pais_categ))
                    print("No se ha encontrado videos de la categoría "+str(categ)+ " del país "+ str(pei))
                else:
                    print("Se ha encontrado un total de "+ str(lt.size(Vids_por_pais_categ))+ " videos.")
                    n=int(input("Escriba la cantidad de videos que desea consultar\n"))
                    lista_organizada=controller.videos_por_algo(Vids_por_pais_categ,n)
                    imprime_toda_lista_econtrada_req1(lista_organizada)


    elif int(inputs[0]) == 4:
        categoria=str(input("Ingrese la categoría que desea consultar \n"))
        if mp.contains(catalog["videos_by_category_id"],str(categoria))==False:
            print_separador()
            print("No se ha encontrado al catgoría "+str(categoria))
            print_separador()
        else:
            Solo_por_categoría=mp.get(catalog["videos_by_category_id"],categoria)
            lista_organizada=controller.videos_por_algo(Solo_por_categoría["value"]["video"],1)
            print_separador()
            print_req3(lista_organizada)
            print_separador()
          

        

                

        
         

    else:
        sys.exit(0)
sys.exit(0)
