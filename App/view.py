﻿"""
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
def imprime_toda_lista_econtrada_req1(catalog):
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
            print(separador())
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
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        controller.loadData(catalog)
        print ("Videos Cargados "+str(controller.sizeLista(catalog["video"])))
        print ("Categorias cargadas "+str(controller.sizeMapas(catalog["category_id"])))
        
       
    elif int(inputs[0]) == 2:
        pei=str(input("Escriba el nombre del país que desea consultar "))
        videos_por_pais=(controller.Getalgobycatalogyllave(catalog["country"],pei))
        vid=videos_por_pais["value"]
        if vid ["Size"]==0:
            print("No se ha encontrado ningun video del país "+ str(pei))
        else:
            categ=str(input("Escriba el numero de la categoria de los videos que desea consultar "))
            print(mp.keySet(vid))

    
        
         

    else:
        sys.exit(0)
sys.exit(0)
