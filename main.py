from classes import *
from menu import *
from funcoes import*

lista_produtos=[]
inicio(lista_produtos)
carrinho = []

close = True

def fluxo_principal():
    while close:
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
                menu_carrinho()
                op = int(input("Qual gostaria: "))
                if op == 1:
                    ver_produtos_carrinho(carrinho)
                elif op == 2:
                    adicionar_produto_carrinho(lista_produtos,carrinho)
                elif op == 3:
                    remover_produto_carrinho(carrinho)
        
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
                excluir_produto(lista_produtos)#esta dando erro
