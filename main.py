from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)
carrinho = []

while True:

    primeiro_menu()
    op = int(input())

    if op == 1:
        print("----- OLÁ CLIENTE ------")

        print("Oque deseja realizar?")
        menu_cliente()
        op = int(input("Qual gostaria: "))
        
        if op == 1:
            imprimir_produtos(lista_produtos)

        elif op == 2:
            pass#selecionar produto
    
    elif op == 2:
        print("----- OLÁ ADMINISTRADOR ------")
        
        print("Oque deseja realizar?")
        menu_adm()
        op = int(input("Qual gostaria: "))
        
        if op == 1:
            adicionar_produto(lista_produtos)
        
        if op == 2:
            pass#editar produto
        
        if op == 3:
            excluir_produto(lista_produtos)#esta dando erro
