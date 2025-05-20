numeros = []  # Lista vazia para armazenar os valores

# Loop para ler 5 valores do usuário
for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))

    # Se a lista estiver vazia ou o número for maior que o último, adiciona no final
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao final da lista.')
    else:
        # Se não for maior, percorre a lista para achar a posição correta
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)  # Insere na posição encontrada
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

# Mostra a lista ordenada
print('-' * 40)
print(f'Os valores digitados em ordem foram: {numeros}')
