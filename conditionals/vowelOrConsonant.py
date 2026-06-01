# Verifica se uma letra informada é vogal, consoante ou nenhum dos dois.

letter = input("Informe uma letra: ")

if letter in 'AEIOUaeiou':
    print("É uma vogal")
elif letter.isalpha():
    print("É uma consoante")
else: 
    print("Não é uma vogal ou uma consoantea")
