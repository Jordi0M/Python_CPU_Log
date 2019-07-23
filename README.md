# Python CPU Log

## Requisitos

1. Tener una versión de Python reciente, la cual contenga PIP (administrador de paquetes)
2. Una vez tengamos Python, instalaremos el paquete "pypiwin32" con pip.
3. Instalar WMI (Instrumentación de Administración Windows)
4. Tener listo para ejecutar el programa OpenHardwareMonitor

## Pequeña Explicación

Se necesitará una versión reciente de Python, para poder ejecutar el administrador de paquetes que lleva Python incorporado, para poder instalar el paquete "pypiwin32", el cual, nos dará acceso a muchas de las API de windows a través de Python.

También tendremos que tener WMI, que es como una base de datos, que guarda unos registros que necesitaremos leer más adelante con Python.

Una vez tengamos todo listo, se necesitará un programa como OpenHardwareMonitor, el cual, guardara toda la información de los sensores que tenga nuestro ordenador, dentro de los registros del WMI.
En caso de que no nos funcione dicho programa, podremos utilizar otro como el CPU Thermometer

## Comandos a realizar

En la terminal de Windows: 

***
    pip install pypiwin32
***

## Ayudas

Para poder saber si se están guardando bien los registros, podemos utilizar WMIExplorer, en el apartado de:

    ROOT\OpenHardwareMonitor
        Sensor

## Ejecución

A la hora de ejecutar el programa, necesitaremos tener en una variable local de Python.
Una vez tengamos la variable local, podremos utilizar un cmd para el archivo “server.py”

***
    python server.py
***

Y necesitaremos otra consola para ejecutar el sensor, pero esta, tendrá que ser con privilegios de administrador

***
    python sensor_mote.py
***
