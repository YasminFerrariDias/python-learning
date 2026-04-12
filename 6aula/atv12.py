# Faça um script em linguagem Python para a leitura de duas notas parciais de um aluno. O script deve calcular a média alcançada por aluno e apresentar:
    
nota1 = int(input('Informe a 1° nota: '))
nota2 = int(input('Informe a 2° nota: '))

media = (nota1 + nota2) // 2

if nota >= 7:
    print('APROVADO')
elif nota <= 7:
    print('REPROVADO')
elif nota == 10:
    print('APROVADO COM DISTINÇÃO')
