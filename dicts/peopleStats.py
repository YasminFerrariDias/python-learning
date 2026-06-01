# Cadastra 4 pessoas com nome, altura e peso, exibindo a menor altura, peso médio e nomes em ordem alfabética.
pessoas = {}
menor_altura = 1000000.0

for i in range(1, 5):
    print(f"PESSOA {i}")
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    dados = []
    dados.append(altura)
    dados.append(peso)
    pessoas.update({nome: dados})

for nome, dados in pessoas.items():
    if dados[0] < menor_altura:
        menor_altura = dados[0]

soma = 0
for nome, dados in pessoas.items():
    soma += dados[1]

media = soma/len(pessoas)
nomes_ordenados = sorted(pessoas.keys())

print("\n" + "="*40)
print("RESULTADOS:")
print("="*40)
print(f"a) Menor altura: {menor_altura:.2f}m")
print(f"b) Peso médio: {media:.2f}kg")
print(f"c) Nomes em ordem alfabética: {nomes_ordenados}")
print("\nDicionário completo:")
print(pessoas)
