casa = float(input('Digite o valor do imóvel: '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
parcela = casa/(anos*12)
minimo = salario*0.30
print(f' Para pagar uma casa de R${casa} em {anos} a prestação sera de R${parcela}')
if parcela > minimo:
     print('Emprestimo negado')
else:
    print('Emprestimo concedido')






