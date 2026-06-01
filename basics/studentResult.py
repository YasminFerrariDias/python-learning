# Calcula a média de duas notas e informa se o aluno foi aprovado ou reprovado.
    
nota1 = int(input('Informe a 1° nota: '))
nota2 = int(input('Informe a 2° nota: '))

media = (nota1 + nota2) // 2

if nota >= 7:
    print('APROVADO')
elif nota <= 7:
    print('REPROVADO')
elif nota == 10:
    print('APROVADO COM DISTINÇÃO')
