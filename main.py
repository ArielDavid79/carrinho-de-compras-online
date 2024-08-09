from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)
carrinho = []

while True:
    primeiro_menu()
<<<<<<< HEAD
    op = int(input())
    #OP ESCOLHIDA IRA ABRIR PAG CLIENTE
=======
    op = int(input("Selecione uma opção: "))

>>>>>>> 79ba862db2cdc2fad20ab6f0fc782016b12c03ac
    if op == 1:
        print("----- OLÁ CLIENTE ------")
        #CRIAR SUB-MENU PARA ABA E MOSTAR ACOES DO CLIENTE
        print("Oque deseja realizar?")
        
        #menu-cliente e fazer as condicoes
        imprimir_produtos(lista_produtos)
<<<<<<< HEAD
    
    #OP ESCOLHIDA IRA ABRIR PAG ADM
=======
        menu_cliente()
        op = int(input("Selecione uma opção: "))
        if op == 1:
            nome_produto = input("Digite o nome do produto: ")
            # quantidade = input("Digite a quantidade do produto: ")
            adicionar_produto_carrinho(lista_produtos,carrinho,nome_produto)
            print(carrinho)
>>>>>>> 79ba862db2cdc2fad20ab6f0fc782016b12c03ac
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
