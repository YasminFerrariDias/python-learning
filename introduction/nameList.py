# Coleta nomes em loop e os exibe como devedores ao final da entrada.
nomes = []
continuar = "S"
while continuar == "S":
    nome = input("Nome: ")
    nomes.append(nome)
    continuar = input("Deseja continuar (S/N)? ")
else:
    for i in nomes:
        print("Devedor: ", i)