# Crie um Script em linguagem Python em Python para calcular a média de três notas inseridas pelo usuário e dar feedback baseado na média calculada.

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
