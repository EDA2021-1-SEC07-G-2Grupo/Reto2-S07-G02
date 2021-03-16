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
    loadVideos(catalog)
    loadVideosCategory(catalog)


def loadVideos(catalog):
    """
    
    """
    videosfile = cf.data_dir + 'Videos/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


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

# Funciones de consulta sobre el catálogo

def categoryIdSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.categoryIdSize(catalog)
    
def videoSize(catalog):
    """
    Numero de libros cargados al catalogo
    """
    return model.videoSize(catalog)
