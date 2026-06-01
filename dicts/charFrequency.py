# Conta a frequência de cada caractere em uma frase e exibe o resultado em um dicionário.
dic = {}

frase = input("Escreva uma frase: ")

for caractere in frase:
    if caractere in dic:
        dic[caractere] = dic.get(caractere, 0) + 1
    else: 
        dic[caractere] = 1

print(dic)
