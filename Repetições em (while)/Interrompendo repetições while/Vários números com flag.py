# Inicializa as variáveis de contagem e soma
soma = 0
cont = 0

while True:  # Loop infinito até o usuário digitar o valor de parada
    num = int(input('Digite um número (999 para parar): '))

    if num == 999:  # Verifica se o número digitado é o valor de parada
        break  # Sai do laço

    soma += num      # Soma o número ao total
    cont += 1        # Conta mais um número digitado

# Mostra o resultado final
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
