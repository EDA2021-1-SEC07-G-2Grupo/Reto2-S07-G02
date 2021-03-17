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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los videos

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'video': None,
               'category_id': None,
               'country': None,
              }

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['video'] = lt.newList('SINGLE_LINKED', comparevideoIds)

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['category_id'] = mp.newMap(49,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapBookIds)
    catalog['country'] = mp.newMap(17,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapBookIds)

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
              "dias": 0,
              }
    Country['name'] = name
    Country['video'] = lt.newList('SINGLE_LINKED', compareCountryByName)
    return Country

def newVidcategoria(name, id):

    categoriavid = {'id': id, 'category_id': name}
    return categoriavid
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):

    lt.addLast(catalog['video'], videos)
    mp.put(catalog['category_id'], videos['category_id'], videos)
    country = videos['country'].split(",")  # Se obtienen los autores
    for pais in country:
        addVideosCountry(catalog, pais.strip(), videos)
    
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
    country['dias'] += 1

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


def compareMapBookIds(id, entry):
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
def categoryIdSize(catalog):
    """
    Número de libros en el catago
    """
    return mp.size(catalog['category_id'])

def videoSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['video'])


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
