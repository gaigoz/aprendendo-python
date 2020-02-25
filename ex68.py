from random import randint

v = 0
while True:
    num = int(input('Diga um valor: '))
    computador = randint(0, 11)
    soma = num + computador
    tipo = ' '
    while tipo not in 'IiPp':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]

    print('-' * 30)
    print(f'Você jogou {num} e o computador {computador}')
    print('-' * 30)

    print('Deu par' if soma % 2 == 0 else 'Deu Impar ')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você Ganhou ')
            v += 1
        else:
            print('Você Perdeu ')
            print('=-' * 15)
            break
    if tipo == 'I':
        if soma % 2 != 0:
            print('Você Ganhou')
            v += 1
        else:
            print('Você perdeu ')
            print('=-' * 15)
            break
    print('Vamos jogar novamente... ')
    print('=-' * 15)


