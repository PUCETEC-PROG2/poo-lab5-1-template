import pytest
import importlib
import sys
import os

class TestAlbum:
    @pytest.fixture
    def artist_module(self):
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        spec = importlib.util.find_spec("artist")
        assert spec is not None, "\n***** El módulo para manejar los artistas no existe. Crea el archivo artist.py. *****\n"
        return importlib.import_module("artist")
    
    @pytest.fixture
    def album_module(self):
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        spec = importlib.util.find_spec("album")
        assert spec is not None, "\n***** El módulo para manejar los álbumes no existe. Crea el archivo album.py. *****\n"
        return importlib.import_module("album")
    
    def test_album_module_exists(self, album_module):
        assert album_module is not None
        
    def test_album_class(self, album_module):
        Album = getattr(album_module, 'Album', None)
        assert Album is not None, "\n***** La clase 'Album' no existe en el módulo album.py. \n\
            Esta debe tener los siguientes atributos: \n\
            1. sku  (número de referencia único): una secuencia de caracteres alfanuméricos que debe ser privado. \n\
            2. 'name' - El nombre del álbum \n\
            3. artist - El ARTISTA del álbum \n\
            3. release_year - El año de lanzamiento\n\
            4. price - El precio: debe ser privado\n\
            5. discount - Un valor de 0  a 0.5 que indica el procentaje de descuento y también debe ser privado. Su valor debe ser 0.0 por defecto\n\
            ****************************\n"
        
    def test_album_invalid_number_of_arguments(self, album_module, artist_module):
        artist_instance = artist_module.Artist(1, "Fleetwood Mac", "Fleetwood Mac es un grupo formado a fines de los 60's")
        Album = album_module.Album
        try:
            Album("123", "Rumours", artist_instance, 1974, 23.22)
        except TypeError as e:
            assert str(e) == "__init__() missing 1 required positional argument: 'description'",\
                "\n***** Faltan argumentos para crear una instancia de Album.\n\
                Asegúrate de pasar los siguientes argumentos en el constructor: id, name, description. ******\n\
                No olvides que debes crear los siguientes atributos: \n\
                1. sku  (número de referencia único): una secuencia de caracteres alfanuméricos que debe ser privado. \n\
                2. 'name' - El nombre del álbum \n\
                3. artist - El ARTISTA del álbum \n\
                3. release_year - El año de lanzamiento\n\
                4. price - El precio: debe ser privado\n\
                5. discount - Un valor de 0  a 0.5 que indica el procentaje de descuento y también debe ser privado. Su valor debe ser 0.0 por defecto\n\
                ****************************\n"
            
    def test_album_attributes(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert album_instance.name == "Wish You Were Here", "\n***** El atributo 'name' del álbum no está siendo inicializado correctamente *****\n"
        assert album_instance.artist == artist_instance, "\n***** El atributo 'artista' del álbum no está siendo inicializado correctamente *****\n"
        assert album_instance.release_year == 1973, "\n***** El atributo 'año' del álbum no está siendo inicializado correctamente *****\n"
        
    def test_album_sku_is_private(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert not hasattr(album_instance, 'sku'), "\n***** El atributo 'sku' del álbum no debe ser público, debe ser privado *****\n"
        
    def test_album_price_is_private(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert not hasattr(album_instance, 'price'), "\n***** El atributo 'price' del álbum no debe ser público, debe ser privado *****\n"
        
    def test_album_discount_is_private(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert not hasattr(album_instance, 'discount'), "\n***** El atributo 'discount' del álbum no debe ser público, debe ser privado *****\n"
    
    def test_album_invalid_sku(self, artist_module, album_module):
        try:
            artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
            album_module.Album(12, "Wish You Were Here", artist_instance, 1973, 22.44)
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que 'sku' solo acepte una cadena en el constructor del álbum *****\n")
            
    def test_album_str(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert str(album_instance) == "Pink Floyd - Wish You Were Here" ,\
            "\t\n***** No has creado la función __str__() en la clase Album.\n\
            Esta debe retornar de la siguiente manera '<nombre_del_artista> - <nombre_del_album>'\
            Ejemplo: 'Soda Stereo - Canción Animal' \
            ****************************\n"
            
    def test_album_get_sku(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'get_sku'), "\n***** La clase Album no tiene el método 'get_sku()' *****\n"
        assert isinstance(album_instance.get_sku(), str), "\n***** El atributo sku debe ser cadena.\
            Además el método 'get_sku()' debe estar creado y devolver una cadena *****\n"
        assert album_instance.get_sku() == "ACB1234", "\n***** El método 'get_sku' no devuelve el valor esperado.\n\
            Recuerda que debe devolver el valor del SKU *****\n"
        
    def test_artist_set_sku(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'set_sku'), "\n***** La clase Album no tiene el método 'set_sku()' *****\n"
        try:
            album_instance.set_sku(34)
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que el set_sku() solo permita setear un string en el sku del álbum *****\n")
            
        try:
            album_instance.set_sku()
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que set_sku() reciba un argumento *****\n")
            
    def test_set_sku_is_correct(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        album_instance.set_sku("ACB8866")
        assert album_instance.get_sku() == "ACB8866", "\n***** set_sku() no está cambiando el valor del SKU del álbum correctamente *****\n"

    def test_album_invalid_price_type_init(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        try:
            album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, "cualquier precio")
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que 'price' solo acepte un FLOTANTE en el constructor del álbum *****\n")
    
    def test_album_negative_price_init(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        try:
            album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, -22.44)
        except ValueError:
            pass
        else:
            pytest.fail("\n***** Asegúrate que el precio del álbum no pueda ser negativo\n Usa una excepción de tipo 'ValueError' para ello *****\n")
    
    def test_album_get_discount(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'get_discount'), "\n***** La clase Album no tiene el método 'get_discount()' *****\n"
        assert isinstance(album_instance.get_discount(), float), "\n***** El atributo de descuento debe ser flotante.\
            Además el método 'get_discount()' debe estar creado y devolver un flotante *****\n"
            
    def test_album_set_discount(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'set_discount'), "\n***** La clase Album no tiene el método 'set_discount()' *****\n"
        try:
            album_instance.set_discount("una_cadena")
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que el set_discount() solo permita setear un flotante en el descuento del álbum *****\n")
    
    def test_album_set_discount_is_valid(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        try:
            album_instance.set_discount(0.9)
        except ValueError:
            pass
        else:
            pytest.fail("\n***** set_discount() no debe permitir valores mayores a 0.5. Usa una excepción de tipo ValueError para ello *****\n")
    
    def test_album_set_discount_negative(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        try:
            album_instance.set_discount(-0.2)
        except ValueError:
            pass
        else:
            pytest.fail("\n***** set_discount() no debe permitir valores negativos. Usa una excepción de tipo ValueError para ello *****\n")
    
    def test_album_get_discount_is_valid(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        album_instance.set_discount(0.4)
        assert album_instance.get_discount() == 0.4, "\n***** get_discount() no está devolviendo el valor esperado,\n\
            Recuerda que éste método debe regresar el valor del atributo 'discount'\
            ****************************\n"
    
    def test_album_get_price(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'get_price'), "\n***** La clase Album no tiene el método 'get_price()' *****\n"
        assert isinstance(album_instance.get_price(), float), "\n***** El atributo de descuento debe ser flotante.\
            Además el método 'get_price()' debe estar creado y devolver un flotante *****\n"
            
    def test_album_set_price(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert hasattr(album_instance, 'set_price'), "\n***** La clase Album no tiene el método 'set_price()' *****\n"
        try:
            album_instance.set_price("una_cadena")
        except TypeError:
            pass
        else:
            pytest.fail("\n***** Debes validar que el set_price() solo permita setear un flotante en el precio del álbum *****\n")
    
    def test_album_set_price_is_valid(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        try:
            album_instance.set_price(-44.2)
        except ValueError:
            pass
        else:
            pytest.fail("\n***** set_price() no debe permitir valores negativos. Usa una excepción de tipo ValueError para ello *****\n")   
            
    def test_album_get_price_is_valid(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        assert album_instance.get_price() == 22.44, "\n**********************************\n\
            get_price() no retorna el valor esperado. Revisa:\n\
                Que set_price() esté asignando el valor correctamente en el atributo del precio\n\
****************************************\n"
    def test_album_get_price_with_discount(self, artist_module, album_module):
        artist_instance = artist_module.Artist(1, "Pink Floyd", "Pink Floyd es un grupo formado a fines de los 60's")
        album_instance = album_module.Album("ACB1234", "Wish You Were Here", artist_instance, 1973, 22.44)
        album_instance.set_discount(0.2)
        assert album_instance.get_price() == 17.952, "\n**********************************\n\
            get_price() no retorna el valor esperado. Revisa:\n\
            que get_price() calcule el valor final del álbum, es decir que aplique el descuento ingresado\n\
****************************************\n"