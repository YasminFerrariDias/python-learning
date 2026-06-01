# Lê números positivos até -1 ser digitado e exibe soma, média, maior e menor usando lista.
import math

i = 1
soma = 0
maior = 0
menor = 0
lista_numero = []

while True:
    numero = int(input(f'Digite o {i}° número positivo: '))
    i += 1
    
    if numero == -1:        
        print('FIM')
        print(f'Os números digitados foi: {lista_numero}')
        print(f'A soma de todos os número é {soma}')
        print(f'O maior número é {maior}')
        print(f'O menor número é {menor}')

        if soma == 0:
            print('Não é possível realizar a média com o valor da soma 0')
        elif i == 0:
            print('Não é possível realizar a média sem ter inserido nenhum valor')
        else:
            media = soma/i
            print(f'A média é {media:.2f}')
        
        break
    elif numero < -1:
        print('Número negativos não são válidos!')
        continue
    else:
        soma += numero
        maior = max(numero, maior)
        menor = min(numero, menor)
        lista_numero.append(numero)
        continue
