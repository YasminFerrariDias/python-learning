# Aplica desconto fixo de 20% sobre o preço de um produto e exibe o valor economizado.
# Sua tarefa é criar um Script em linguagem Python que pede o preço original de um produto e dá 20% de desconto. Você deve mostrar: Preço original do produto Valor do desconto em R$ (tipo 'Você ganhou R$ xx,xx de desconto’) Valor do produto com o desconto

preco = float(input("Informe o preço original de um produto: "))

desconto = preco * (20 / 100)
total = preco - desconto

print("O preço do produto é de %.2f reais." % (preco))
print("O seu desconto é de %.2f reais." % (desconto))
print("O valor do produto com desconto é de %.2f reais." % (total))
 
