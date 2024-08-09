def primeiro_menu():
    print("Selecione uma opção!")
    print("1 - Cliente\n2 - Adiministrador\n")

def imprimir_produtos(lista_produtos):
    for item in lista_produtos:
        print(f"Nome: {item.nome}")
        print(f"Valor: {item.preco}")
        print(f"Quantidade: {item.quantidade}\n")


def menu_adm():
    print("1 - Adiconar produto\n2 - Editar produto\n3 - Excluir produto")