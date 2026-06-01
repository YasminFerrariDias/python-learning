# Lê números positivos até -1 ser digitado e exibe a lista, total e média.
numeros = []
total = 0

while True: 
    numero = int(input("Digite um número positivo (para sair, digite -1): "))
    
    if numero >= 0:
        numeros.append(numero)
    elif numero == -1:
        print(numeros)
        break
    else: 
        print("Número inválido, é aceito apenas números positivos e o -1!")

for i in numeros:
    total += i

quant = len(numeros)
media = total/quant

print(f"Total: {total}")
print(f"Média: {media}")
