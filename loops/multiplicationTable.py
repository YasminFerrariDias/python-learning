# Exibe a tabuada completa de um número informado pelo usuário, de 0 a 10.
N = int(input("Digite o número que deseja ver a tabuada: "))

print(f"Tabualda de {N}")
for i in range(0, 11):
    resultado = N * i
    print(f"{N} x {i} = {resultado}")
