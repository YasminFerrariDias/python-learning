# Calcula a média de três notas e exibe feedback com base no resultado.

nota1 = float(input("Informe a 1° nota: "))
nota2 = float(input("Informe a 2° nota: "))
nota3 = float(input("Informe a 3° nota: "))

media = 3 / (nota1 + nota2 + nota3)

if media >= 7.0:
    print(f"{media:.2f} - Parabéns! Sua média é alta.")
elif media >= 5.0:
    print(f"{media:.2f} - Sua média é razoável.")
elif media < 5.0:
    print(f"{media:.2f} - Sua média é baixa. É uma boa oportunidade para melhorar.")
