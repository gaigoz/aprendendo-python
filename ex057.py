sexo = str(input('Digite seus sexo [M/F]: ')).strip()
while sexo not in 'MmFf':
   sexo = str(input('Dados inválidos, digite novamente')).strip()
print('Cadastro realizado com sucesso')
