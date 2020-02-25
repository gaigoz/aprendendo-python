from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

if computador == 0: #computador pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHA')
    elif jogador == 2:
        print('COMPUTADOR GANHA')
    else:
        print('opção inválida')
if computador == 1: #computador pedra
    if jogador == 0:
        print('COMPUTADOR GANHA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
    else:
        print('opção inválida')

if computador == 2: #computador pedra
    if jogador == 0:
        print('JOGADOR GANHA')
    elif jogador == 1:
        print('COMPUTADOR GANHA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('opção inválida')