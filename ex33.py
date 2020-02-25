a = int(input('digite uma numero: '))
b = int(input('digite uma numero: '))
c = int(input('digite uma numero: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O maior salario é é {maior}')
print(f'Menor salario é {menor}')