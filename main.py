from classes import *
from menu import *
from funcoes import*


lista_produtos=[]
inicio(lista_produtos)
carrinho = []

def fluxo_principal():
    close = True
    while close:
        primeiro_menu()
        op = int(input("Insira uma opção: "))
        if op == 1:
            fluxo_cliente()
        elif op == 2:
            fluxo_adm()
        elif op == 0:
            close = False
        else:
            print("Opção não encontrada! ")

def fluxo_cliente():
    close = True
    while close:
        menu_cliente()
        op = int(input("Insira uma opção: "))
        if op == 1:
            ver_produtos(lista_produtos)
        elif op == 2:
            fluxo_cliente_op2()
        elif op == 0:
            close = False
        else:
            print("Opção não encontrada! ")

def fluxo_cliente_op2():
        close = True
        while close:
            menu_carrinho()
            op = int(input("Insira uma opção: "))
            if op == 1:
                ver_produtos_carrinho(carrinho)
            elif op == 2:
                adicionar_produto_carrinho(lista_produtos,carrinho)
                sub_menu_adicionar_produto_carrinho()
                op = int(input("Insira uma opção: "))
                while op == 1:
                    adicionar_produto_carrinho(lista_produtos,carrinho)
                    sub_menu_adicionar_produto_carrinho()
                    op = int(input("Insira uma opção: "))
                if op == 0:
                    close = False
            elif op == 3:
                remover_produto_carrinho(carrinho)
            elif op == 0:
                close = False
            else:
                print("Opção não encontrada! ")

def fluxo_adm():
    close = True
    while close: 
        menu_adm()
        op = int(input("Insira uma opção: "))     
        if op == 1:
            adicionar_produto(lista_produtos)  
        elif op == 2:
            editar_produto(lista_produtos)
        elif op == 3:
                excluir_produto(lista_produtos)
        elif op == 4:
            ver_produtos(lista_produtos)
        elif op == 0:
            close = False

fluxo_principal()
