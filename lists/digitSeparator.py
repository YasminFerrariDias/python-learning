# Recebe um número entre 100 e 999 e exibe cada dígito separadamente.
numero = input("Digite um número inteiro entre 100 e 999: ")

if numero.isdigit() and 100 <= int(numero) <= 999:
    for i in numero:
        print(i)
else: 
    print("Valor inválido!")
