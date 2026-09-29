#! /usr/bin/env python3

"""
Printando as letras do abecedário, via character unicode
"""


print ("Printando as letras do abecedário")

numero = list(range(64, 128))
for numeros in numero:
    if numeros > 64 and numeros < 91:
        letra = (chr(numeros))
        print(f"A letra {letra} maisculas corresponde ao número {numeros} em ASCII")
    elif numeros > 96 and numeros <= 122:
        letra = (chr(numeros))
        print(f"A letra {letra} minuscula corresponde ao número {numeros} em ASCII")
    else:
        a = "1"





