# Generador de cartones de bingo

[![Build Status](https://travis-ci.com/fromant65/AAT.svg?branch=master)](https://travis-ci.com/fromant65/AAT)

Este proyecto tiene la intención de, utilizando Python como lenguaje de programación, dar distintas funciones que tengan la capacidad de generar un cartón de Bingo tradicional. El proyecto es llevado a cabo para la asignatura de Adaptacion al Ambiente de trabajo (AAT) de la especialidad Informatica, en el Instituto Politécnico Superior Gral San Martin, Rosario, Santa Fe, Argentina.

## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:

* Cada carton es una matriz de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* Cada columna debe tener una o dos celdas ocupadas obligatoriamente.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Requisitos
Para utilizar esta app se requerirá tener instalados los siguientes programas:
* PIP
* Python
* Git

## Clonar el repositorio
Para clonar el repositorio, deberemos crear una carpeta en donde deseemos y nos quede mas cómodo.
Una vez creada la carpeta, abrimos una terminal en dicha carpeta y ejecutamos el siguiente código
<pre><code>git clone https://github.com/fromant65/AAT.git</pre></code>
Esto solo debe realizarse la primera vez que obtenemos los archivos.

## Actualizar el repositorio
Para actualizar el repositorio en nuestra maquina local entramos en la carpeta donde clonamos los archivos y ejecutamos:
<pre><code>git pull origin master</pre></code>

## Ubicación
En src/<br>
Programa que genera el talonario de bingo.

En test/<br>
Tests que validan el funcionamiento del src.

## Ejecución

Para ejecutar el programa, en una terminal deberemos ejecutar el siguiente comando:
<pre><code>python bingo.py</pre></code>

## Comentarios 
Agradecimientos a Mariano D'Agostino, profesor encargado de la asignatura.
