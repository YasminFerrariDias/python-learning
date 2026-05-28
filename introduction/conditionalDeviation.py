# Calcula a média de preço por idade de uma pessoa com base nos dados informados.
idade = int(input("Idade: "))
preco = float(input("Preço: "))
nome = input("Nome: ")
preco_idade = preco / idade
print("Média de preço por idade do", nome, "é ", preco_idade)