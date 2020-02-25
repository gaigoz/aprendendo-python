numero = int(input('Digite um numero para ver sua tabuada: '))
cont = 1
for n in range(1, 11):
    resultado = numero * cont
    print(f'{numero} X {cont} = {resultado}')
    cont = cont + 1
