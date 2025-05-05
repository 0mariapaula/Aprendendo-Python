tota = cont = num = 0
while num != 999:
    num = int(input('Digite um numero [999 pra parar]:'))
    if num != 999:
        tota += num
        cont += 1
    if num == 999:
        print('A soma total dos {} numero/s que voce digitou é {}'.format(cont,tota))
        print('Se contassemos o 999 teriamos {} numeros'.format(cont + 1))
        print('Progama finalizado')