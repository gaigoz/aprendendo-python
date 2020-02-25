numero = int(input('Digite um numero de até 4 digitos: '))
unidade = (numero%1000)%10
dezena = ((numero%1000)//10)%10
centena = (numero%1000)//100
milhar = (numero//1000)


print(f'Milhar:  {milhar}')
print(f'Centena  {centena}')
print(f'Dezena:  {dezena}')
print(f'Unidade: {unidade}')
