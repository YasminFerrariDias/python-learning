# A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas, 10% em outras, nada em outros produtos e até 30% em alguns outros produtos. Crie um Script em Python que pergunte o preço original e o desconto que deve ser concedido. Ele deve mostrar a saída igual ao exercício anterior.

preco = float(input("Informe o preço original de um produto: "))
porcentagem = float(input("Informe o desconto desse produto (em porcentagem): "))

desconto = preco * (porcentagem / 100)
total = preco - desconto

print("O preço do produto é de %.2f reais." % (preco))
print("O seu desconto é de %.2f reais." % (desconto))
print("O valor do produto com desconto é de %.2f reais." % (total))
 
 
