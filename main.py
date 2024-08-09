from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)

while True:
    primeiro_menu()
    op = int(input())
    #OP ESCOLHIDA IRA ABRIR PAG CLIENTE
    if op == 1:
        print("----- OLÁ CLIENTE ------")
        #CRIAR SUB-MENU PARA ABA E MOSTAR ACOES DO CLIENTE
        print("Oque deseja realizar?")
        
        #menu-cliente e fazer as condicoes
        imprimir_produtos(lista_produtos)
    
    #OP ESCOLHIDA IRA ABRIR PAG ADM
    elif op == 2:
        print("----- OLÁ ADMINISTRADOR ------")
        
        print("Oque deseja realizar?")
        menu_adm()
        op = int(input("Qual gostaria: "))
        
        if op == 1:
            adicionar_produto(lista_produtos)
        
        if op == 2:
            pass
        
        if op == 3:
            excluir_produto(lista_produtos)
