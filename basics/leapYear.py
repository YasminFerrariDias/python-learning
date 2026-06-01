# Verifica se um ano informado é bissexto com base nas regras de divisibilidade.

ano = int(input('Informe um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é um ano bisexto.')
else:
    print(f'O ano {ano} não é um ano bisexto.')

