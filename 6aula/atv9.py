# Criar um script em linguagem Python que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = int(input('Informe o quanto você ganha por hora: '))
horas = int(input('Informe a quantidade de horas que você trabalha: '))

salario = valor * horas

print(f'O seu salário é de R${salario}')
