# Lê N números informados pelo usuário e calcula a média aritmética.
N = int(input("Digite a quantidade de número a informar: "))

soma = 0

for count in range(N):
    num = float(input("Digite um número: "))
    soma += num

media = soma/N
print(f"Média = {media:.2f}")
