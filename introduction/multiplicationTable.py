# Exibe a tabuada de um número informado pelo usuário, de 1 a 10.
numero = int(input("Digite o número da tabuada que deseja saber: "))

for i in range(1, 11):
    print(i, ' x ', numero, ' = ', i*numero)
