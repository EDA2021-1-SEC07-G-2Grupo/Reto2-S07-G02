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
    print("-----------------------------------------------(T(工)T)--------------------------------------------")


def imprime_toda_lista_econtrada_req1(catalog,size):
    print(print_separador())
    n=1
    while n<=size:
            video_ordenado=lt.getElement(catalog,n)
            print("Posición: "+str(n))
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
    vid=lt.getElement(catalog,1)
    print("-"+"Title: "+vid["title"])
    print("-"+"Channel title: "+vid["Channel title"])
    print("-"+"Category ID: "+vid["ID"])
    print("-"+"Días: "+str(vid["dias"]))

def print_req4(catalog,size):
    n=1
    print_separador()
    while size>=n:
            vid=lt.getElement(catalog,n)
            print("Video "+str(n))
            print("-"+"Title: "+vid["title"])
            print("-"+"Chanel_title: "+vid["channel_title"])
            print("-"+"Publish_time: "+vid["publish_time"])
            print("-"+"Likes: "+vid["likes"])
            print("-"+"Dislikes: "+vid["dislikes"])
            print("-"+"Tags: "+vid["tags"])
            print_separador()
            n+=1
   

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

        print_separador()    
        print("Cargando información de los archivos ....")
        
        catalog = controller.initCatalog()
        espacio_tiempo=controller.loadData(catalog)
        print ("Videos Cargados "+str(controller.sizeLista(catalog["video"])))
        print ("Categorias cargadas "+str(controller.sizeMapas(catalog["category_id"])))

    elif int(inputs[0]) == 2:
        print_separador()    
        pei=str(input("Escriba el nombre del país que desea consultar \n"))
        if mp.contains(catalog["country"], pei)== False:
            print_separador()
            print("No se ha encontrado ningun video del país "+ str(pei))
            print_separador()
        else:
            videos_por_pais=(controller.Getalgobycatalogyllave(catalog["country"],pei))
            categ=str(input("Escriba el numero de la categoria de los videos que desea consultar: \n"))
            categ=" "+categ
            if mp.contains(catalog["category_id"],str(categ))==False:
                print_separador()
                print("No se ha encontrado ninguna categoría "+ str (categ))
                print_separador()
            else:
                num=mp.get(catalog["category_id"],categ)
                Vids_por_pais_categ=controller.Getvideosbycateg(videos_por_pais,num["value"]["category_id"])
                if lt.isEmpty(Vids_por_pais_categ)==True:
                    print(lt.size(Vids_por_pais_categ))
                    print("No se ha encontrado videos de la categoría "+str(categ)+ " del país "+ str(pei))
                else:
                    print("Se ha encontrado un total de "+ str(lt.size(Vids_por_pais_categ))+ " videos.")
                    n=int(input("Escriba la cantidad de videos que desea consultar\n"))
                    lista_organizada=controller.videos_por_algo(Vids_por_pais_categ,n,"views")
                    imprime_toda_lista_econtrada_req1(lista_organizada,n)

    elif int(inputs[0]) == 3:
        TODO:print("req 2")
        pass


    elif int(inputs[0]) == 4:
        print_separador()    
        categoria=str(input("Ingrese la categoría que desea consultar \n"))
        categoria=" "+ categoria
        num=mp.get(catalog["category_id"],categoria)
        num=num["value"]["category_id"]
        print_separador()
        if mp.contains(catalog["videos_by_category_id"],str(num))==False:
            print_separador()
            print("No se ha encontrado la catgoría "+str(categoria))
            print_separador()
        else:
            
            Solo_por_categoría=mp.get(catalog["videos_by_category_id"],num)
            agrupacion=controller.agrupacion_id(Solo_por_categoría["value"]["video"])
            print("Cargando información de los archivos ....")
            lista_organizada=controller.videos_por_algo(agrupacion,5,"dias")
            print_separador()
            print_req3(lista_organizada)
            print_separador()
          

    elif int(inputs[0]) == 5:
        pais=str(input("Escriba el pais que quiere consultar "))
        
        if mp.contains(catalog["country"],pais)==False:
            print_separador()
            print("No se ha encontrado el pais que está cosultado ")
            print_separador()
        else:
            lista_por_pais=mp.get(catalog["country"], pais)
            categoria_cosultar=str(input("Escriba el tag que desea consultar "))
            lista_filtrada=controller.get_video_by_tag(lista_por_pais,categoria_cosultar)
            if lt.size(lista_filtrada)==0:
                print_separador()
                print("No se a encontrado ningún video con el tag "+str(categoria_cosultar) )
                print_separador()
            else:
                print("Se ha encontrado un total de "+str(lt.size(lista_filtrada)))
                n=int(input("Escriba la cantidad de videos que desea consultar "))
            
                lista_organizada=controller.videos_por_algo(lista_filtrada,n,"likes")
                print_req4(lista_organizada,n)
         
    
    else:
        sys.exit(0)
sys.exit(0)
