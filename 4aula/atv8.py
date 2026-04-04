# Elabore um Script em linguagem Python que leia uma frase, uma palavra 
# antiga e uma palavra nova. O Script deve exibir uma string contendo a frase 
# original e outra com a ocorrência da palavra antiga substituída pela palavra 
# nova.

frase = input("Digite uma frase: ")
antiga = input("Digite uma palavra que tenha na frase: ")
nova = input("Digite uma palavra nova: ")

novo = frase.replace(antiga, nova)

print(frase)
print(novo)
