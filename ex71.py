valor = int(input('valor: R$ '))

nota50 = 50

nota50 = valor // 50
valor = valor % 50

nota20 = valor // 20
valor = valor % 20

nota10 = valor // 10
valor %= 10

nota1 = valor // 1

print(f'{nota50} notas de 50 R$')
print(f'{nota20} notas de 20 R$')
print(f'{nota10} notas de 10 R$')
print(f'{nota1} notas de 1 R$')