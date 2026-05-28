# Verifica se uma pessoa está apta a doar sangue com base em saúde, peso, alimentação e horas de sono.
saude = str(input("Você está em boas condições de saúde? (S/N) "))
peso = float(input("Você está pesando quantos quilos? "))
alimentacao = str(input("Você está alimentado? (S/N) "))
sono = float(input("Você dormiu quantas horas nas últimas 24h? "))

if (saude == "S" or saude == "s") and peso >= 50 and (alimentacao == "S" or alimentacao == "s") and sono >= 6:
    print("Parabéns, você pode ser um doador!!")
else:
    print("Sentimos muito, nesse momento você não pode doar.")
