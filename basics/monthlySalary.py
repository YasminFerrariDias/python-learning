# Calcula o salário mensal com base no valor por hora e nas horas trabalhadas.

valor = int(input('Informe o quanto você ganha por hora: '))
horas = int(input('Informe a quantidade de horas que você trabalha: '))

salario = valor * horas

print(f'O seu salário é de R${salario}')
