def primeiro_menu():
    print("""\n----- LOGIN ------
1 - Cliente\n2 - Administrador\n0 - Sair\n""")

def menu_adm():
    print("""\n----- OLÁ ADMINISTRADOR ------
1 - Adicionar produto\n2 - Editar produto\n3 - Excluir produto\n4 - Ver produtos\n0 - Voltar\n""")

def menu_cliente():
    print("""\n----- OLÁ CLIENTE ------
1 - Ver produtos\n2 - Meu carrinho\n0 - Voltar\n""")

def menu_carrinho():
    print("""\n----- OPÇÕES CARRINHO ------
1 - Ver carrinho\n2 - Adicionar produtos\n3 - Remover produtos\n0 - Voltar\n""")
    
def sub_menu_adicionar_produto_carrinho():
    print("""\n----- OPÇÕES ------
1 - Adicionar mais produtos\n0 - Voltar\n""")