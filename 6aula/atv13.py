#Elabore um script em linguagem Python que leia três números e mostre o maior deles.

numero1 = int(input('Informe o 1° número: '))
numero2 = int(input('Informe o 2° número: '))
numero3 = int(input('Informe o 3° número: '))

maior = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

print(f'O maior número é o {maior}')
