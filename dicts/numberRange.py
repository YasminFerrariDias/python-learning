# Gera e exibe uma lista com todos os inteiros entre dois valores informados pelo usuário.
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

resultado = []

for i in range(x, y + 1):
    resultado.append(i)
    
print(resultado)
