# Jogo de adivinhar o número sorteado em até 10 tentativas.
from random import randint

max = 10
tentativas = 0

num_sorteado = randint(1, 100)

num = 0

while (tentativas < 10) and (num_sorteado != num):
    print(f'Você tem {max - tentativas}, chances!')

    num = int(input("Adivinhe o número sorteado(1 a 100): "))

    if num > num_sorteado:
        print(f"O número sorteado é menor que {num}")
    elif num < num_sorteado:
        print(f"O número sorteado é maior que {num}")
    tentativas += 1
    
if num == num_sorteado:
    print(f"Parabéns, você acertou o número sorteado em {tentativas} vezes!")
else:
    print(f'Não foi desta vez! {num_sorteado}')
