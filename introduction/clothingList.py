# Coleta nome, valor e quantidade de roupas em loop e exibe um resumo formatado ao final.
nomes = []
valors = []
quantidades = []

continuar = "S"
while continuar.upper() == "S":
    nome = input("Nome da roupa: ")
    valor = float(input("Valor: "))
    quantidade = int(input("Quantidade: "))
    
    nomes.append(nome)
    valors.append(valor)
    quantidades.append(quantidade)
    
    continuar = input("Deseja continuar (S/N)? ")

print("\nResumo dos Itens:")
for n, v, q in zip(nomes, valors, quantidades):
    print(f"Roupa: {n}, Valor: R$ {v:.2f}, Quantidade: {q}.")
