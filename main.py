from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)

while True:
    primeiro_menu()
    op = int(input())

    if op == 1:
        imprimir_produtos(lista_produtos)
    elif op == 2:
        adicionar_produto(lista_produtos)