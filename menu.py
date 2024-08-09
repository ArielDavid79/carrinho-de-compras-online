def primeiro_menu():
    print("1 - Cliente\n2 - Administrador\n")

def imprimir_produtos(lista_produtos):
    for item in lista_produtos:
        print(f"\nNome: {item.nome}")
        print(f"Valor: {item.preco}")
<<<<<<< HEAD
        print(f"Quantidade: {item.quantidade}\n")


def menu_adm():
    print("1 - Adiconar produto\n2 - Editar produto\n3 - Excluir produto")
=======
        print(f"Quantidade: {item.quantidade}")

def menu_cliente():
    print("\n1 - Meu carrinho\n")
>>>>>>> 79ba862db2cdc2fad20ab6f0fc782016b12c03ac
