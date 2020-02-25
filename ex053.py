word = str(input('Digite uma palavra')).strip()
if word == word[::-1]:
    print('é palindromo')
else:
    print('não é palindromo')
print(word)
print(word[::-1])