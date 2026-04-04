# Elabore um Script em linguagem Python que solicite uma frase ao usuário e 
# escreva a frase toda em maiúscula. No mesmo Script exiba a frase sem espaços 
# em branco. Dica use replace.

frase = input("Digite uma frase: ")

maiuscula = frase.upper()
final = maiuscula.replace(" ", "")

print(final)
