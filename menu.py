def primeiro_menu():
    print("1 - Cliente\n2 - Administrador\n")

def imprimir_produtos(lista_produtos):
    for item in lista_produtos:
        print(f"\nNome: {item.nome}")
        print(f"Valor: {item.preco}")
        print(f"Quantidade: {item.quantidade}\n")


def menu_adm():
    print("1 - Adiconar produto\n2 - Editar produto\n3 - Excluir produto")

def menu_cliente():
    print("1 - Ver produtos\n2 - Carrinho\n")


def menu_carrinho():
    print("1 - Ver carrinho\n2 - Adicionar produtos\n3 - Remover produtos")