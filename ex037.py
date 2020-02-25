num = int(input('Digite um numero: '))
print('''Escolha com das opções
[1] converter para bínario
[2] converter para octal
[3] converter para hexadecimal''')
op = int(input('Digite sua opção: '))
if op == 1 or op == 2 or op == 3:
    print('Opção válida')
    if op == 1:
     print(f'{num} Convertido para binário é igual a {bin(num)[2:]} ')
    if op == 2:
     print(f'{num} Convertido para binário é igual a {oct(num)[2:]}')
    if op == 3:
     print(f'{num} Convertido para binário é igual a {hex(num)[2:]}')
else:
    print('Opção inválida')
