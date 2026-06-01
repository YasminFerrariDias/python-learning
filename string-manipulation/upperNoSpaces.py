# Converte uma frase para maiúsculas e remove todos os espaços em branco.
frase = input("Digite uma frase: ")

maiuscula = frase.upper()
final = maiuscula.replace(" ", "")

print(final)
