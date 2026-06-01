# Converte um número decimal para hexadecimal, binário e octal.

numero = int(input('Informe um número decimal: '))

print(f'Decimal: {numero}')
print(f'Hexa: {hex(numero)[2:].upper()}')
print(f'Binário: {bin(numero)[2:]}')
print(f'Octal: {oct(numero)[2:]}')
