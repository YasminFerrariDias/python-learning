# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 35%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para X cópias? Solicite o valor de X. Crie um Script em linguagem Python para solicitar os dados necessários e exibir o custo total da compra

copias = int(input("Informe a quantidade de copias que deseja comprar: "))

valor_livros = copias * 24.95
frete = ((copias - 1) * 0.75) + 3
desconto = valor_livros * 0.35

total = valor_livros - desconto + frete

print(f'O custo total da compra é de R$ {total:.2f}')                   
