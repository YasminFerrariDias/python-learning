# Cadastra três produtos com descrição e preço e exibe o mais caro.
dic = {}

for i in range(1, 4):
    descricao = input(f"Descrição do {i}° produto: ")
    preco = float(input(f"Preço do {i}° produto: "))

    dados = []
    dados.append(preco)
    dic.update({descricao: dados})

maior = 0.0
produto_caro = ''
for descricao, dados in dic.items():
    if dados[0] > maior:
        maior = dados[0]
        produto_caro = descricao

print(f"O produto mais caro é o {produto_caro} com o preço R$ {maior:.2f}")
