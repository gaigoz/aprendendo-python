num = int(input('Digite um numero inteiro: '))
c = num
fat = 1
while c > 0:
    print(f'{c}', end=' ')
    print('x ' if c > 1 else ' = ', end='')
    fat = fat * c
    c += -1
print(fat)