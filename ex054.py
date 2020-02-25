from datetime import date
atual = date.today().year
cont1 = 0;
cont2 = 0;
for n in range(1, 8):
    nascimento = int(input('Qual seu ano de nascimento? '))
    idade = atual - nascimento
    if idade >= 21:
        cont1+=1
    else:
        cont2+=1
print(f'maior {cont1} e menor {cont2}')
