# Elabore um Script em linguagem Python que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M – Masculino ou Sexo Inválido.

letter = input("Informe um gênero (M/F): ")

if letter == 'F':
    print("F - Feminino")
elif letter == 'M':
    print("M - Masculino")
else: 
    print("Sexo Inválido")
