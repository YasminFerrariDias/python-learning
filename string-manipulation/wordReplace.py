# Substitui uma palavra em uma frase por outra informada pelo usuário e exibe ambas as versões.
frase = input("Digite uma frase: ")
antiga = input("Digite uma palavra que tenha na frase: ")
nova = input("Digite uma palavra nova: ")

novo = frase.replace(antiga, nova)

print(frase)
print(novo)
