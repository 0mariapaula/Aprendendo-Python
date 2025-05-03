#  Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes
from time import sleep
print("-="*20, '\nAnalisando triângulo:')
print('-='*20)
r1 = float(input('Medida do primero lado: '))
r2 = float(input('Medida do segundo lado: '))
r3 = float(input('Medida do terceiro lado: '))
sleep(2)
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com essas medidas é possivel formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é \033[31mEQUILÁTERO\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é \033[31mISÓSCELES\033[m.')
    else:
        print('O triângulo formado é \033[31mESCALENO\033[m.')
else:
    print('Com essas medidas não é possivel formar um triângulo.')

