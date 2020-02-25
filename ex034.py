salario = float(input('Digite seu salario'))

if salario >= 1250:
    print(f'Seu novo salario com 10% é:  R$ {salario*1.10}')
else:
    print(f'Seu novo salario com 15% é:  R$ {salario * 1.15}')