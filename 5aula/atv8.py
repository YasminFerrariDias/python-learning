# Criar um Script em linguagem Python que ajuda a verificar se um parafuso está apertado corretamente de acordo com o torque especificado. O torque é uma medida de força rotacional aplicada a um objeto, e é especialmente importante na engenharia mecânica para garantir a segurança das montagens

aplicado = float(input("Insira o valor do torque aplicado (em Nm):"))
recomendado = float(input("Insira o valor do torque de aperto recomendado (em Nm):"))

diferenca = abs(recomendado - aplicado)
comparado = recomendado * 0.10

if diferenca <= comparado:
    print("O parafuso está apertado corretamente.")
else: 
    print("O parafuso não está apertado corretamente.")
