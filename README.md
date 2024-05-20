# Laboratorio 5

Eres un desarrollador para una tienda de discos de música y te han pedido que crees el catálogo de una manera amigable. En este ejercicio, tu tarea es crear dos clases en Python: Artist y Album.

## Objetivo
El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) como: Clases, Ojetos, Atributos, Métodos, creación de instancias; así como los 4 princicios del POO como son: Encapsulación, Abstracción, Herencia y Polimorfismo

## Paso 1: Crear la clase 'Artist'

Para comenzar, necesitamos registrar los artistas musicales disponibles para catalogar los álbumes. Cada artista debe tener los siguientes campos:

- id - ID único del sistema: un número entero que será privado.
- name - Nombre del Género.
- description - Descripción.

Además, la clase Artist debe tener implementado el método \__str__(), que devuelve el nombre del Artista.

## Paso 2: Crear la clase 'Album'

La clase Trainer debe tener los siguientes atributos:

- sku - SKU (número de referencia único): una secuencia de caracteres alfanuméricos que debe ser privado.
- name - Nombre del Álbum.
- artist - El artista del álbum
- release_year - Año de lanzamiento.
- price - El precio del disco: debe ser privado.
- discount - El descuento del álbum: por defecto es 0 y el rango de dicho descuento no debe ser mayor a 0.5. También debe ser privado.

### Particularidades de los métodos de la clase 'Album'

- Debes añadir los getters y setters que consideres necesarios.
- El método get_precio() debe devolver el precio final del álbum aplicando el descuento correspondiente.
- Además, la clase 'Album' debe tener implementado el método \__str__(), que devuelve el nombre de la siguiente manera: "siguiente manera '<nombre_del_artista> - <nombre_del_album>". Ejemplo: "The Beatles - Let it Be"

## Paso 3. Modificación de \_\_main\_\_.py
En el método "classes_manual_tests()" del archivo "\_\_main\_\_.py" se especifican las actividades a realizar, esto permitirá verificar la comprensión del estudiante acerca de la creación de las instancias de las clases, y el uso adecuado de las mismas

## ¿Cómo realizar las pruebas?

Para realizar las prueba de este repositorio debes ejecutar el siguiente comando

## Instalación del ambiente
### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## ¿Cómo ejecutar las pruebas?

Las pruebas automatizadas en este repositorio están están en los siguientes archivos:
- tests/01_artist_test.py
- tests/02_album_test.py

**Importante: Debes tener activado el ambiente virtual tal como se indica en el paso anterior**

Para realizar las prueba de este repositorio debes ejecutar los siguientes scripts:

- Para ejecutar un archivo de prueba concreto
    ~~~ 
    pytest tests/01_artist_test.py
    ~~~

- Para ejecutar todas las pruebas
    ~~~ 
    pytest
    ~~~


## Notas adicionales

Para cada clase, asegúrate de que los atributos estén correctamente inicializados en el constructor (\_\_init\_\_()).
Puedes definir métodos adicionales en cada clase si lo consideras necesario.
Después de crear las clases, puedes usarlas para crear instancias de Album y Artist según las pruebas proporcionadas.
¡Buena suerte!
