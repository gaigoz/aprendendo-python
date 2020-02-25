print('Loja Barata')
barato = ' '
total = qnt = menor = cont = 0
while True:

    prod = str(input('Nome do Produto: '))
    valor = int(input('Preço: '))
    cont += 1
    total += valor

    if prod > 1000:
        qnt += 1

    if cont == 1 or valor < menor:
        menor = valor
        barato = prod

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S|N] ')).strip().upper()[0]
    if op == 'N':
        break
