# Lê números positivos até -1 e exibe soma, quantidade, média, maior e menor.
quantidade = 0
maior = None
menor = None
acumulador = 0

while True:
    numero = int(input("Digite número positivos: "))
    if numero > 0:
        acumulador += numero
        quantidade += 1
        media = acumulador/quantidade

        if maior is None:
            maior = numero
            menor = numero
        
        if numero > maior:
            maior = numero
            
        if numero < menor:
            menor = numero
    elif numero == -1:
       print(f"Soma: {acumulador}")
       print(f"Quantidade: {quantidade}")
       print(f"Média: {media}")
       print(f"Maior: {maior}")
       print(f"Menor: {menor}")
       break
    else:
        print("Insira um valor válido! ")
        break
