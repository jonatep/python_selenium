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

# Generación de reportes

Con la configuración por defecto del ``runner.py`` se generarán reportes acerca de la ejecución de los tests. Pero para poder visualizarlos hay que cumplir una serie de pasos previos. 

## 1. Instalación de Allure-Commands

Allure se instala junto al resto de los módulos a través del ``requirements.txt``, pero no es suficiente para generar y visualizar sus reportes. En [la página oficial de Allure](https://allurereport.org/docs/gettingstarted-installation/) hay distintas formas de instalarlo para que la consola de Windows reconozca sus comandos.

## 2. NPM

En caso de instalar Allure a través de NPM, como ha sido mi caso, para primero generar los reportes hay que ejecutar los tests con el depurador de VSCode, o ejecutando esta línea:

`````python
behave -f allure_behave.formatter:AllureFormatter -o reports ./features
`````

En este caso se generarán los JSONs de datos en la carpeta ``reports``.

Una vez los JSONs se ejecuten, se pueden visualizar los análisis. 

``npx allure serve reports``

Esto creará un directorio temporal donde se almacenará la página web, y la abrirá en el navegador automáticamente.
