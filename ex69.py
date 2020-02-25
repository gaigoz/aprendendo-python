print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)

maiores = homem = mulher = 0

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        mulher += 1

    if idade > 18:
        maiores += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break

print(f'Mulheres com menos de 20 anos: {mulher}')
print(f'Pessoas com menos de 18 anos: {maiores}')
print(f'Homens: {homem}')
