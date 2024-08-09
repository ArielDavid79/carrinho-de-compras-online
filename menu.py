def primeiro_menu():
    print("1 - Cliente\n2 - Administrador\n")

def imprimir_produtos(lista_produtos):
    for item in lista_produtos:
        print(f"\nNome: {item.nome}")
        print(f"Valor: {item.preco}")
        print(f"Quantidade: {item.quantidade}")

def menu_cliente():
    print("\n1 - Meu carrinho\n")