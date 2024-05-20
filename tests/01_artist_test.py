# tests/test_artist.py

import pytest
import importlib
import sys
import os

class TestArtist:
    @pytest.fixture
    def artist_module(self):
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        spec = importlib.util.find_spec("artist")
        assert spec is not None, "\n***** El módulo para manejar los géneros musicales no existe. Crea el archivo artist.py. *****\n"
        return importlib.import_module("artist")

    def test_artist_module_exists(self, artist_module):
        assert artist_module is not None
        
    def test_artist_class(self, artist_module):
        Artist = getattr(artist_module, 'Artist', None)
        assert Artist is not None, "\n***** La clase 'Artist' no existe en el módulo artist.py. \n\
            Esta debe tener los siguientes atributos: \n\
            1. id de tipo entero (privado) \n\
            2. name \n\
            3. description \n\
            ****************************\n"
        
    def test_artist_invalid_number_of_arguments(self, artist_module):
        Artist = artist_module.Artist
        try:
            Artist(1, "The Beatles", "desc")
        except TypeError as e:
            assert str(e) == "__init__() missing 1 required positional argument: 'description'",\
                "\n***** Faltan argumentos para crear una instancia de Artist.\n\
                Asegúrate de pasar los siguientes argumentos en el constructor: id, name, description. ******\n\
                No olvides que debes crear los siguientes atributos: \n\
                    1. id de tipo entero (privado) \n\
                    2. name de tipo cadena \n\
                    3. description de tipo cadena \n\
                    ****************************\n"
        
    def test_artist_attributes(self, artist_module):
        Artist = artist_module.Artist
        artist_instance = Artist(1, "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        assert artist_instance.name == "Pink Floyd", "\n***** El atributo 'name' del artista no está siendo inicializado correctamente en  *****\n"
        assert artist_instance.description == "Pink floyd es un grupo formado a fines de los 60's",\
                            "\n***** El atributo 'description' no está siendo inicializado correctamente *****\n"
                            
    def test_artist_private_id(self, artist_module):
        Artist = artist_module.Artist
        artist_instance = Artist(1, "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        assert not hasattr(artist_instance, "id"), "\n**** El atributo 'id' del artista no debería ser público ****\n"
            
    def test_artist_invalid_id(self, artist_module):
        Artist = artist_module.Artist
        try:
            Artist("One", "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que el id solo acepte enteros en el constructor del artista *****\n")
            
    def test_artist_str(self, artist_module):
        Artist = getattr(artist_module, 'Artist', None)
        artist_instance = Artist(1, "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        assert str(artist_instance) == "Pink Floyd", "\n***** \
            Debes crear el método '__str__()' en 'Artist' y este debe retornar el nombre del artista\
            "
            
    def test_artist_get_id(self, artist_module):
        Artist = artist_module.Artist
        artist_instance = Artist(3, "The Rolling Stones", "The Rolling Stones es un grupo formado por Mick Jagger y Keith Richards")
        assert hasattr(artist_instance, 'get_id'), "\n***** La clase Artist no tiene el método 'get_id()' *****\n"
        assert isinstance(artist_instance.get_id(), int), "\n***** El atributo id debe ser entero.\
            Además el método 'get_id()' debe estar creado y devolver un entero *****\n"
        assert artist_instance.get_id() == 3, "\n***** El método 'get_id' no devuelve el valor esperado del ID *****\n"
        
        
    def test_artist_set_id(self, artist_module):
        Artist = artist_module.Artist
        artist_instance = Artist(1, "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        assert hasattr(artist_instance, 'set_id'), "\n***** La clase Artist no tiene el método 'set_id()' *****\n"
        try:
            artist_instance.set_id("dos")
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que el id solo acepte enteros en set_id() *****\n")
            
        try:
            artist_instance.set_id()
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que set_id() reciba un argumento *****\n")
            
    def test_set_id_is_correct(self, artist_module):
        Artist = artist_module.Artist
        artist_instance = Artist(1, "Pink Floyd", "Pink floyd es un grupo formado a fines de los 60's")
        artist_instance.set_id(3)
        assert artist_instance.get_id() == 3, "\n***** set_id() no está cambiando el valor del id correctamente *****\n"