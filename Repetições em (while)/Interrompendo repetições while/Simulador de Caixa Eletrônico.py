print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor  # Valor que ainda falta sacar
cedula = 50    # Começamos com a cédula de maior valor
total_cedulas = 0  # Contador de cédulas da vez

while True:
    # Enquanto o valor total ainda for maior ou igual à cédula atual
    if total >= cedula:
        total -= cedula        # Subtrai o valor da cédula do total
        total_cedulas += 1     # Conta mais uma cédula
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédula(s) de R${cedula}')
        
        # Troca a cédula para a próxima menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0  # Zera o contador de cédulas para a nova cédula

        # Se o valor total chegar a zero, encerra
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO PYTHON! Tenha um bom dia!')
