# Selenium-Behave en Python

En este README se detallará la instalación del proyecto y el uso de sus distintas funcionalidades.


# Instalación

## 1. Python

La versión a instalar de Python será la `3.12.1`, y se podrá descargar a través de su [página web](https://www.python.org/). Se debe instalar el entorno de Python junto a **pip**, para gestionar las librerias.

## 2. Librerías

Se aconseja crear un [entorno virtual](https://docs.python.org/es/3/library/venv.html) para instalar las librerías necesarias. estando dentro de la carpeta del proyecto, ejecutamos:

    pip install -r requirements.txt

  

# Ejecución de tests

Hay dos formas de ejecutar los tests.

## 1. Línea de comandos

Estando dentro de la carpeta del proyecto, ejecutando:

    behave

Si queremos ejecutar los tests con la etiqueta 'test', o la que queramos, sería:

    behave --tags="@test"
    
## 2. Depurador de VSCode

Configurando un archivo ``launch.json`` en VSCode podremos personalizar cómo se ejecutan los archivos Python. En este proyecto el archivo de configuración ideal sería:

       {
    
	    "name": "Python: Behave",
	    
	    "type": "python",
	    
	    "request": "launch",
	    
	    "module": "behave",
	    
	    "console": "integratedTerminal",
	    
	    "args": [
	    
		    "--no-capture",
		    
		    "--no-capture-stderr",
		    
		    "--no-skipped",
		    
		    "--tags=\"@test\""
	    
	    ]
    
    }
En caso de querer ejecutar todos los tests habría que eliminar la línea de ``"--tags=\"@test\""``. Una vez configurado este archivo, se puede ejecutar estando en el archivo ``runner.py``

## Ajustes en ejecución

En el archivo ``environment.py`` se puede ajustar el navegador web en el que ejecutar los tests y el tiempo de "timeout" de los mismos. Para ello hay que modificar el valor de las variables:

- ``os.environ['DRIVER_BROWSER']``
	- ``'chrome'``: Ejecutar Google Chrome
	- ``'firefox'``: Ejecutar Mozilla Firefox
	- ``'edge'``: Ejecutar Microsoft Edge
	- ``'safari'``: Ejecutar Safari
 - ``os.environ['TIMEOUT']``
 	- El valor deseado

  También es posible especificar o el navegador o el timeout, no ambos a la vez, en el comando de ejecución de los tests de behave. Simplemente hay que añadir al comando 'behave':

  - ``-D browser=navegador``, siendo las opciones de 'navegador' las mostradas previamente
  - ``-D timeout=tiempo``

 En caso de haber especificado un navegador o timeout tanto como variable de entorno como a través del comando, el valor especificado en el comando behave tendrá preferencia. 
 
# Generación de reportes

Con la configuración por defecto del ``runner.py`` se generarán reportes acerca de la ejecución de los tests. Pero para poder visualizarlos hay que cumplir una serie de pasos previos. 

## 1. Instalación de Allure-Commands

Allure se instala junto al resto de los módulos a través del ``requirements.txt``, pero no es suficiente para generar y visualizar sus reportes. En [la página oficial de Allure](https://allurereport.org/docs/gettingstarted-installation/) hay distintas formas de instalarlo para que la consola de Windows reconozca sus comandos.

## 2. NPM

Gracias al archivo ``behave.ini`` cada vez que se ejecuten los tests los reportes necesarios se añadirán automáticamente a la carpeta ``allure-results``. En caso de no querer que se generen estos archivos de reportes, hay que borrar el archivo ``behave.ini``

Una vez se ejecuten los tests, se pueden visualizar los análisis. 

``npx allure serve``

Esto creará un directorio temporal donde se almacenará la página web, y la abrirá en el navegador automáticamente.

# Análisis de código

Para ejecutar el análisis de código de ``pylint``, una vez instalado a través del ``requirements.txt``, ejecutar el siguiente comando:

``pylint <carpeta> --disable=C,R``

Donde ``<carpeta>`` es el nombre de la carpeta a analizar. Por ejemplo, ``pages`` o ``features``. 
