# Desenvolva um Script em linguagem Python que leia uma frase e um 
# caractere. Em seguida, exiba ambos e o número de ocorrências do caractere na 
# frase.

frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

qtd = frase.count(caractere)

print("O caractere {} aparece {} no código".format(caractere, qtd))
