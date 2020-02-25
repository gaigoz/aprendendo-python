num = int(input('Digite um numero: '))
fat = 1
for c in range(num, 0, -1):
    print(f'{c}', end=' ')
    print('x ' if c > 1 else ' = ', end='')
    fat *= c
print(fat)