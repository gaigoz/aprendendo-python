vel = int(input('Qual era a velocidade do carro? '))
if vel > 80:
    print('Você foi multado haha')
    multa = (vel-80) * 7
    print(f' Sua multa sera de R$ {multa}')
else:
    print('você não foi multado, continue assim')