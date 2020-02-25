import math

an = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(an))
coseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f' Seno {seno:.2f} \n Cosseno {coseno:.2f} \n Tangente {tangente:.2f}')