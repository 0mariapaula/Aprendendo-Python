# Criando uma lista vazia para armazenar os números únicos
numeros = []

# Loop infinito para permitir que o usuário digite vários números
while True:
    # Lê um número inteiro do usuário
    num = int(input('Digite um número: '))
    
    # Verifica se o número ainda não foi adicionado na lista
    if num not in numeros:
        numeros.append(num)  # Se não estiver na lista, adiciona
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado! Não vou adicionar.')  # Se já estiver, avisa que não será adicionado

    # Pergunta ao usuário se deseja continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    # Se o usuário digitar algo diferente de "S", o laço será encerrado
    if continuar != 'S':
        break

# Linha decorativa para separar visualmente a saída final
print('-' * 40)

# Exibe a lista com os números digitados, em ordem crescente
print(f'Você digitou os valores: {sorted(numeros)}')
