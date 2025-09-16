def contador (i, f, p):
   print (f'Contagem de {i} até {f} de {p} em {p}:')

   if i < f:
       cont = i
       while cont <= f:
           print (f'{cont}', end=' ', flush=True)
           cont += p
   else:
       cont = i
       while cont >= f:
           print (f'{cont}', end=' ', flush=True)
           cont -= p
   print('FIM!')

contador (1,10,1)
contador (10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)


