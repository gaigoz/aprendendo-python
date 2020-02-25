nome = str(input('Digite seu nome')).strip()
lista = nome.split()
ultimo = lista[-1]
print(f'Seu primeiro nome é {lista[0]} e seu ultimo nome é {lista[-1]}')