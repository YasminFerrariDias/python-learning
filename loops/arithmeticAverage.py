# Calcula a média aritmética de 4 números informados pelo usuário via loop while.
soma = 0
quantidade = 0

while quantidade < 4:
    numero = int(input("Informe um número: "))

    soma += numero
    media = soma/4
    quantidade += 1
    
print(f"A média aritmética é {media}")
