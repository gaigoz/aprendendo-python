n = int(input('Quantos termos de fibo você quer? '))
num1 = 0
num2 = 1
cont = 3
print(f'{num1} -> {num2}', end =' ')
while cont <= n:
    num3 = num1+num2
    print(f'-> {num3}', end=' ')
    num1 = num2
    num2 = num3
    cont += 1
print('chega')