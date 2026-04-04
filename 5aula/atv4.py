# Escreva um Script em linguagem Python que verifique se uma letra digitada é vogal ou consoante. Ou ainda se não está nestes grupos.

letter = input("Informe uma letra: ")

if letter in 'AEIOUaeiou':
    print("É uma vogal")
elif letter.isalpha():
    print("É uma consoante")
else: 
    print("Não é uma vogal ou uma consoantea")
