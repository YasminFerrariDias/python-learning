# Calcula o salário líquido descontando IR (11%), INSS (8%) e sindicato (5%).

valor = int(input('Informe o quanto você ganha por hora: '))
horas = int(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = valor * horas

imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

desconto = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - desconto

print(f'Salário bruto: {salario_bruto}')
print(f'INSS: {inss}')
print(f'Sindicato: {sindicato}')
print(f'Salário líquido: {salario_liquido}')
