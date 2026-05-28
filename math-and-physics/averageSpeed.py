# Calcula a velocidade média de um objeto com base no deslocamento e na variação de tempo.
# Construa um Script em linguagem Python que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o Script deve calcular a velocidade média, em m/s, do objeto. Mostrar os dados fornecidos e o valor calculado.


deslocamento = float(input("Informe o deslocamento do objetos (em metros): "))
segundos = float(input("Informe a variação de tempo (em segundos): "))

velocidade_media = deslocamento/segundos

print("DESLOCAMENTO em metros: %.2f" % (deslocamento))
print("VARIAÇÃO DO TEMPO em segundos: %.2f" % (segundos))
print("A velocidade média é de: %.2f" % (velocidade_media))
