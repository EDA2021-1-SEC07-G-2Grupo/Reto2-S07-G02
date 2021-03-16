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
               'video_id': None,
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
    catalog['video_id'] = mp.newMap(49,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapBookIds)

    return catalog




# Funciones para creacion de datos

def newVidcategoria(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    categoriavid = {'id': id, 'category_id': name}
    return categoriavid
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['video'], videos)
    mp.put(catalog['video_id'], videos['video_id'], videos)
    


def addVideoCategory_id(catalog, category):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo y se
    actualiza el indice de identificadores del tag.
    """

    newtag = newVidcategoria(category['id'], category['name'])
    mp.put(catalog['video_id'], category['id'], newtag)



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
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
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







# Funciones de consulta
def categoryIdSize(catalog):
    """
    Número de libros en el catago
    """
    return mp.size(catalog['video_id'])

def videoSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['video'])


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
