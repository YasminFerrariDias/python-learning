# Elabore um Script em linguagem Python que leia o nome do usuário e mostre 
# o nome de traz para frente, utilizando somente letras maiúsculas.

nome = input("Digite seu nome: ")

maior = nome.upper()

print(maior[::-1])
