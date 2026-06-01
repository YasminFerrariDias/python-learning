# Lê três números e exibe o maior e o menor entre eles.

numero1 = int(input('Informe o 1° número: '))
numero2 = int(input('Informe o 2° número: '))
numero3 = int(input('Informe o 3° número: '))

maior = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

menor = numero1

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
