soma = media = qnt = menor = maior = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    qnt += 1
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Deseja continuar? [S/N] ")).strip()[0]
print(soma/qnt)
print(maior)
print(menor)

