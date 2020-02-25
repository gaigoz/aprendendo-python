while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        resultado = num * c
        print(f'{num} X {c} = {resultado}')
    print('-' * 30)
print('Encerrado')

