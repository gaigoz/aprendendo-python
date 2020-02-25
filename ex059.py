num = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero: '))
op = 0
while op != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    ''')
    op = int(input('>>>>Digite umas das opções: '))
    if op == 1:
        soma = num + num2
        print(f'A soma entre {num} e {num2} é {soma}')
    elif op == 2:
        prod = num * num2
        print(f'A multiplicação entre {num} e {num2} é {prod}' )
    elif op == 3:
        if num > num2:
            print(f'O maior é {num}')
        else:
            print(f'O maior é {num2}')
    elif op == 4:
        num = int(input('Digite um numero:'))
        num2 = int(input('Digite outro numero: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
print('Fim do programa')