soma = cont = 0

while True:
    num = int(input('Digite um nuemro: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma é {soma} e foram digitados {cont} nuúmeros')