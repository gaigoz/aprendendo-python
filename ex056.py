totidade = 0
contM = 0
velho = ''
idademaior = 0
for n in range(1,5):
    print(f'{n}ª Pessoa')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper().strip()
    totidade += idade
    if n == 1 and sexo == 'M':
        idademaior = idade
        velho = nome
    if sexo.find('M') and idade > idademaior:
        idademaior = idade
        velho = nome
    if sexo == 'F' and idade < 20:
            contM += 1
total = (totidade) / 4
print(f'Média de idade do grupo de pessoas é de {total} anos')
print(f'O homem mais velhor tem {idademaior} e se chama {velho}')
print(f'Ao todo são {contM} mulheres com menos de 20 anos')

# if n == 1 and sexo in 'Mn' isso também serve parar comparar se é igal