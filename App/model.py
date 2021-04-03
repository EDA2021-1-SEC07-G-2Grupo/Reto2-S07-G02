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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog():
   
    catalog = {'video': None,
               'category_id': None,
               'country': None,
               "videos_by_category_id":None
              }
    catalog['video'] = lt.newList('ARRAY_LIST', comparevideoIds)


    catalog['category_id'] = mp.newMap(39,
                                   maptype='PROBING',
                                   loadfactor=0.8,
                                   comparefunction=comparebyName)
    catalog['country'] = mp.newMap(17,
                                   maptype='PROBING',
                                   loadfactor=0.8,
                                   comparefunction=comparebyName)
    catalog['videos_by_category_id'] = mp.newMap(39,
                                   maptype='PROBING',
                                   loadfactor=0.8,
                                   comparefunction=comparebyINt)

    return catalog




# Funciones para creacion de datos
def newCountry(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    Country = {'name': "",
              "video": None,
              "Size": 0,
              }
    Country['name'] = name
    Country['video'] = lt.newList('ARRAY_LIST', compareCountryByName)
    return Country


def newcateg(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    videos_by_category_id = {'name': "",
              "video": None,
              }
    videos_by_category_id['name'] = name
    videos_by_category_id['video'] = lt.newList('ARRAY_LIST', compareCountryByName)
    return videos_by_category_id


def newVidcategoria(name, id):

    categoriavid = {'id': id, 'category_id': name}
    return categoriavid
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    
    lt.addLast(catalog['video'], videos)
    mp.put(catalog['category_id'], videos['category_id'], videos)
    country = videos['country'].split(",")  # Se obtienen los paises
    videos_by_category_id = videos['category_id'].split(",")  #obtener por categoría
    for pais in country:
        addVideosCountry(catalog, pais.strip(), videos)
    for categ in videos_by_category_id:
        addVideosCategory_id(catalog, categ.strip(),videos)
    
def addVideosCountry(catalog, pais, videos):

    countries = catalog['country']
    existenciacountry = mp.contains(countries, pais)
    if existenciacountry:
        entry = mp.get(countries, pais)
        country = me.getValue(entry)
    else:
        country = newCountry(pais)
        mp.put(countries, pais, country)
    lt.addLast(country['video'], videos)
    country['Size'] += 1


def addVideosCategory_id(catalog, catego, videos):
    
    numcategs = catalog['videos_by_category_id']
    existencicateg = mp.contains(numcategs, catego)
    if existencicateg:
        entry = mp.get(numcategs, catego)
        categ = me.getValue(entry)
    else:
        categ = newcateg(catego)
        mp.put(numcategs, catego, categ)
    lt.addLast(categ["video"],videos)
    
    
        
        
def addVideoCategory_id(catalog, category):

    newtag = newVidcategoria(category['id'], category['name'])
    mp.put(catalog['category_id'], category['id'], newtag)




#----------------------------
# Funciones de Comparación
#----------------------------
def comparevideoIds(id1, id2):
    """
    Compara dos ids de dos libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def comparebyINt(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if int(id) == int(identry):
        return 0
    elif int(id) > int(identry):
        return 1
    else:
        return -1


def comparebyName(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (id) == identry:
        return 0
    elif (id > identry):
        return 1
    else:
        return -1



def compareTagNames(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1

def compareCountryByName(keyname, pais):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    country = me.getKey(pais)
    if (keyname == country):
        return 0
    elif (keyname > country):
        return 1
    else:
        return -1




# Funciones de consulta



def Getalgobycatalogyllave(catalog, pais): 
    return mp.get(catalog,pais)









# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento



def videos_por_algo(catalog,size,comparacion):
    sub_list = lt.subList(catalog,0, size)
    sub_list = sub_list.copy()
    sorted_list=merg.sort(sub_list, comparacion)
    return  sorted_list

