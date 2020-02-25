frase = str(input(' Digite uma frase: ')).strip()
print(frase.count('a'))
print(f' A letra "a" aparece pela primeira vez na {(frase.find("a"))} posição')
print(f' A letra "a" aparece pela ultima vez na {(frase.rfind("a"))} posição')
