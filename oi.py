#! /usr/bin/env python3

# Criando comentário que preste no código ###

"""Dependendo da lingua configurada no ambiente o programa
exibe a correspondente
"""

"""Como usa:
Tenha a variável LAN devidamente confgiurada ex:
    export LANG=pt_BR

Execução:
    python3 oi.py
    ou
    ./oi.py
"""

# Dunder

""" O Dunder é o double underline palavra e double underline, ele é utilizado por alguns programas de empacotamento 
para listar versão, entre outras informações gerais da aplicação
"""
__version__ = "0.0.1"
__author__ = "Felipe Silveira"
__license__ = "Unlicense"


import os


# Código

"""
A variavel current_language está buscando a variável do sistema LANG e pegando somente os primeiros 5 caracteres dela
Caso essa variavel LANG não exista no Sistema Operacional, por padrão será considerado o en_US
"""
current_language = os.getenv("LANG", "en_US")[:5]
message =  "Hello World !"

if current_language == "pt_BR":
    message = "Olá Mundo !"
elif current_language == "it_IT":
    message = "Ciao, Mondo !"
else:
    message = "É...deu BO"

print(message)
