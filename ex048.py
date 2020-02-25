soma = 0
for n in range(1, 501, 2):
    if n % 2 != 0:  # não precisaria
        if n % 3 == 0:
            soma = soma + n
            print(n, end=' ')
print(f'A soma é {soma}')

