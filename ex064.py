soma = 0
cont = 0
num = int(input('Digite um numero: '))
while num != 999:
    soma +=num
    cont+=1
    num = int(input('Digite um numero: '))
print(f'Foram digitados {cont} termos e sua soma é {soma}')