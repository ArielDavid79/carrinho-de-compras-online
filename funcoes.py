from classes import *

def inicio(lista_produtos):
    produto=Produto("Arroz",27.99,7)
    lista_produtos.append(produto)

    produto=Produto("Feijão",7.99,7)
    lista_produtos.append(produto)

    produto=Produto("Macarrão",5.99,7)
    lista_produtos.append(produto)

    produto=Produto("Ovo",12.99,7)
    lista_produtos.append(produto)

    produto=Produto("Leite",5.99,7)
    lista_produtos.append(produto)
    
def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    for item in lista_produtos:
        if item.nome == nome:
            while item.nome == nome:
                print("Produto já cadastrado!")
                nome = input("Digite o nome do produto: ")
                
    preco = input("Digite o preço do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    

    produto = Produto(nome,preco,quantidade)
    lista_produtos.append(produto)

def excluir_produto(lista_produtos):
    produto_nome = input("Qual produto deseja excluir: ")
    for item in lista_produtos:
        if item.nome == produto_nome:
            lista_produtos.remove(produto_nome)
            print("Produto excluido!")
        if item.nome != produto_nome:
            print("Nome não encontrado!")
            
