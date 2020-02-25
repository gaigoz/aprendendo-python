from datetime import date
atual = date.today().year
born = int(input('Qual seu ano de nascimento'))
idade = atual - born

if idade == 18:
    print('Esta na hora de você se alistar ')
elif idade < 18:
    print(f'faltam {18-idade} anos para você se alistar')
else:
    print(f' Ja se passaram {idade-18} anos do seu alistamento')
