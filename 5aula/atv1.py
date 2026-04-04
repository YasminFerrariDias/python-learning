# Desenvolva um Script em linguagem Python que solicite dois números quaisquer e
# mostre o maior entre eles.

n1 = int(input("Informe o 1° número: "))
n2 = int(input("Informe o 2° número: "))

if n1 == n2:
    print("Os número {} e {} são iguais".format(n1, n2))
elif n1 > n2:
    print("O número {} é maior que {}.".format(n1, n2))
elif n1 < n2:
    print("O número {} é maior que {}.".format(n2, n1))
else:
    print("Insira valores válidos!")
