# Exibe nome completo, cidade, estado e data de nascimento do usuário formatados.

nome = input("Informe seu nome completo: ")
cidade = input("Informe sua cidade: ")
estado = input("Informe seu estado: ")
dia = input("Informe o dia do seu nascimento: ")
mes = input("Informe o mes do seu nascimento: ")
ano = input("Informe o ano do seu nascimento: ")

print("Olá", nome, "!")
print("Você mora na cidade", cidade, "que é localizado no estado de", estado, ".")
print("Você nasceu em", end=' ')
print(dia, mes, ano, sep='/')

