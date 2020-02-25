maior = 0
menor = 999
for n in range(1, 6):
    peso = float(input('Digite pesos aleatóros: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'maior {maior}')
print(f'menor {menor}')
