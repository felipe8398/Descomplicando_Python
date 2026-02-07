#! /usr/bin/env python3

"""
Mostrar a tabuada do 1 ao 10

Tabuada do 1
1
2
3
4
5
6
7
8
9
10
------
Tabuada do 2
2
4
6
8
10
12
14
16
18
20
"""

__author__ = "Felipe"
__version_ = "0.1.0"

base = list(range(1, 11))

for numero in base:
    Multiplicadores = list(range(1, 11))
    print("Tabuada do número:", numero)
    for Multiplicador in Multiplicadores:
        Resultado = numero * Multiplicador
        print(numero, "*", Multiplicador, "=", Resultado)
    print("-----------------------------")
