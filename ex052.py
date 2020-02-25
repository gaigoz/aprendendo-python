cont = 0
num = int(input('Digite um valor: '))
for n in range(1, num + 1):
    if num % n == 0:
        print('Divisilvel: ', end='')
        cont = cont +1
    else:
        print('Não divisivel: ', end='')
    print(n)
print(f'O numero {num} foi divisivel {cont} vezes ')
if cont == 2:
    print('É primo ')
else:
    print('não é primo')