soma = 0
for n in range(1, 7):
    val = int(input('Digite um valor'))
    if val % 2 == 0:
        soma = soma + val
print(f'A soma é {soma}')