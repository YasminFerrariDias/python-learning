# Cadastra contatos com nome, idade, endereço e telefone em um dicionário e os exibe ao final.
d = {}

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")

    dados = []
    dados.append(idade)
    dados.append(endereco)
    dados.append(telefone)
    d.update({nome: dados})

    resposta = input("Sair S/N?")
    if resposta == "S" or resposta == "s":
        break
    elif resposta == "N" or resposta == "n":
        continue
    else:
        print("Insira valores válidos!")

print(d)
