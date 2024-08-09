from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)
carrinho = []

while True:
    primeiro_menu()
    op = int(input("Selecione uma opção: "))

    if op == 1:
        imprimir_produtos(lista_produtos)
        menu_cliente()
        op = int(input("Selecione uma opção: "))
        if op == 1:
            nome_produto = input("Digite o nome do produto: ")
            # quantidade = input("Digite a quantidade do produto: ")
            adicionar_produto_carrinho(lista_produtos,carrinho,nome_produto)
            print(carrinho)
    elif op == 2:
        adicionar_produto(lista_produtos)