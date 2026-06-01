# Verifica se o torque aplicado em um parafuso está dentro da tolerância de 10% do valor recomendado.

aplicado = float(input("Insira o valor do torque aplicado (em Nm):"))
recomendado = float(input("Insira o valor do torque de aperto recomendado (em Nm):"))

diferenca = abs(recomendado - aplicado)
comparado = recomendado * 0.10

if diferenca <= comparado:
    print("O parafuso está apertado corretamente.")
else: 
    print("O parafuso não está apertado corretamente.")
