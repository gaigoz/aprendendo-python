numero = float(input('Distancia em KM: '))
if numero <= 200:
    print(f' Preço da passaagem: {numero*0.50}')
else:
    print(f'Preço da passagem acima de 200km: {numero*0.45}')
