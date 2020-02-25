import random
from time import sleep
numero = random.randint(0, 5)
print('-+-' * 20)
print('Vou pensar em um numero e tente adivinhar')
print('-+-' * 20)
numeroUser = int(input('Digite um numero e tente a sorte...'))
print('PROSSESANDO RESULTADO...')
sleep(3)
if numero == numeroUser:
    print(f'Parabéns você acertou')
else:
    print(f'Mais sorte na proxima o numero correto era {numero} ')