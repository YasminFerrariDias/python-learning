# Desenvolver um script em linguagem Python que leia a velocidade máxima permitida em uma avenida e a velocidade com que o motorista estava dirigindo por ela.

velocidade_maxima = int(input("Informe a velocidade máxima permitida: "))
velocidade_motorista = int(input("Qual a velocidade que o motorista estava: "))

ultrapassou = velocidade_motorista - velocidade_maxima

if ultrapassou <= 0:
    print('Vel. Normal.')
elif ultrapassou > 0 and ultrapassou <= 10:
    print(f'Você ultrapassou à {ultrapassou} km/h acima do permitido, sua multa é de R$ 85,13.')
    print('Multa leve: -3 pontos na carteira')
elif ultrapassou >= 11 and ultrapassou <= 30:
    print(f'Você ultrapassou à {ultrapassou} km/h acima do permitido, sua multa é de R$ 127,69.')
    print('Multa média: -5 pontos na carteira')
elif ultrapassou > 30:
    print(f'Você ultrapassou à {ultrapassou} km/h acima do permitido, sua multa é de R$ 574,62.')
    print('Multa gravíssima: -7 pontos na carteira')
