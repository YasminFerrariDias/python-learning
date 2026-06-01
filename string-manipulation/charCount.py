# Conta o número de ocorrências de um caractere em uma frase.
frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

qtd = frase.count(caractere)

print("O caractere {} aparece {} no código".format(caractere, qtd))
