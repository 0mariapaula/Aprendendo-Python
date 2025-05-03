soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0: #multiplos de 3 
            soma += c
            cont += 1
print('A soma de todos os{} valores solicitados e {}'.format(cont,soma))
