import random
tent = 0
numero = random.randint(0, 10)
print('Escolha um numero de 0 a 10 e tente a sorte')
jogador = int(input('Qual o seu palpite: '))
while numero != jogador:
    print(numero)
    if jogador < numero:
        print('Mais... Tente novamente')
    else:
        print('Menos... Tente novamente')
    jogador = int(input(' Qual o seu palpite: '))

    tent +=1
print(f'Acertou com {tent+1} tentativas ')

