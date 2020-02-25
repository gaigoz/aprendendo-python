dias = int(input(" Por quantos dias o carro foi utilizado? "))
km = int(input(' Quantos kilometros foram rodados com o carro?'))

valorPago = (km*0.15)+(dias*60)

print(f' O valor pelo aluguel do carro sera {valorPago:.2f}')
