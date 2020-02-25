print(f'{"Lojas Jaggi":=^40}')

valor = float(input('Qual o valor a ser pago pelo produto: '))
print('''
[1] A vista/cheque
[2] A vista no cartão
[3] Em até 2x no cartão sem juros
[4] Em 3x  ou mais no cartão com juros
''')
op = int(input('Escolha uma das opções: '))

if op == 1:
    desconto =valor - (valor*0.1)
    print(f'O valor fica R$ {desconto} com 10% de desconto')
elif op == 2:
    desconto = valor - (valor * 0.05)
    print(f'O valor fica R$ {desconto} com 5% de desconto')
elif op == 3:
    parcela = valor/2
    print(f'O valor do fica em 2x de R$ {parcela} sem juros')
elif op == 4:
    total = valor*1.20
    totalparcelas = int(input('Em quantas vezes deseja parcelar? '))
    parcela = (valor*1.20)/totalparcelas
    print(f'Em {totalparcelas}x o valor fica R$ {total} com parcelas de R$ {parcela} ')