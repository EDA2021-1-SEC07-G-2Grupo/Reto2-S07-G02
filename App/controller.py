"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort as merg
import time
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadVideosCategory(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory


def loadVideos(catalog):
    """
    
    """
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    lista_prohibido=lt.newList(datastructure="ARRAY_LIST")
    for video in input_file:
        model.addVideo(catalog,video,lista_prohibido)
        


def loadVideosCategory(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    videocategoryfile = cf.data_dir + 'Videos/category-id.csv'
    input_file = csv.DictReader(open(videocategoryfile, encoding='utf-8'), delimiter='\t')
    for videotag in input_file:
        model.addVideoCategory_id(catalog, videotag)

# Funciones para la carga de datos

# Funciones de ordenamiento
def videos_por_algo(catalog,size,comparacion):
    if comparacion=="views":
        def cmpVideosByviews(video1, video2):

            return (float(video1["views"]) > float(video2["views"]))
        comparacion=cmpVideosByviews
    elif comparacion=="dias":
         def cmpVideosBydias(video1, video2):
             return (float(video1["dias"]) > float(video2["dias"]))
         comparacion=cmpVideosBydias

    elif comparacion=="likes":
         def cmpVideosBylikes(video1, video2):

             return (float(video1["likes"]) > float(video2["likes"]))
         comparacion=cmpVideosBylikes


    return model.videos_por_algo(catalog,size,comparacion)

# Funciones de consulta sobre el catálogo

def sizeMapas(catalog):
    """
    Número de libros en el catago
    """
    return mp.size(catalog)

def sizeLista(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog)

def Getalgobycatalogyllave(catalog, pais):
    return model.Getalgobycatalogyllave(catalog,pais)


def Getvideosbycateg(catalog,numero):
    lista_filtrada=lt.newList("ARRAY_LIST")
    i = 1
    while i <= (lt.size(catalog["value"]["video"])):
        wow=lt.getElement(catalog["value"]["video"],i)
        if numero==wow["category_id"] or str(numero)== wow ["category_id"]:
            lt.addLast(lista_filtrada, wow)
        i+=1
   
    return lista_filtrada


def get_video_by_tag(catalog,tag):
    lista_filtrada=lt.newList("ARRAY_LIST")
    i=1
    while i <= lt.size(catalog["value"]["video"]):
        a =lt.getElement(catalog["value"]["video"],i)
        if tag in a["tags"]:
            lt.addLast(lista_filtrada,a)
        i+=1
    return lista_filtrada
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()
def agrupacion_id(catalog):
        lista_prohibido=lt.newList(datastructure="ARRAY_LIST")
        lista_organizada=lt.newList(datastructure="ARRAY_LIST")
        i=1
        while i <= lt.size(catalog):
            videos=lt.getElement(catalog,i)
            ID=videos["video_id"]
            dato={"ID": ID,"title":videos["title"], "Channel title": videos["channel_title"], "country":videos["country"],"dias":1}
            precencia=lt.isPresent(lista_prohibido,ID)
            if precencia>0:
                precencia_en_la_main=lt.getElement(lista_prohibido,precencia+1)
                el_cambio=lt.getElement(lista_organizada,int(precencia_en_la_main))
                el_cambio["dias"]+=1
            else:
                lt.addLast(lista_prohibido,ID)
                lt.addLast(lista_organizada,dato)
                a=str(lt.size(lista_organizada))
                lt.addLast(lista_prohibido,a)
            i+=1  
        return lista_organizada

def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory


