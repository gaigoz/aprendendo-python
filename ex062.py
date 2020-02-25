termo = int(input('Digite um termo incinial: '))
razao = int(input('digite a razão: '))
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} -> ', end=' ')
        termo = termo + razao
        c+=1
    print('pause')
    mais = int(input('Quantos termos a mais ? '))
print('acabou')