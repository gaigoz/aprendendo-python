nome = 'Vinicius Jaggi'.strip()
print(f'Seu nome em caixa alta {nome.upper()}')
print(f'Seu nome em Minusculo {nome.lower()}')
print(f'Seu nome tem: {len(nome)-nome.count(" ")} letras')
print(f'letras no primeiro nome: {nome.find(" ")}')
#Outra maneira de fazer a contagem das letras do primeiro nome
lista = nome.split()
print(f'nome: {len(lista[0])} letras')



