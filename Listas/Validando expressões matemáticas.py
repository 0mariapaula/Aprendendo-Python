# Função para verificar se os parênteses estão balanceados
def verificar_parenteses(expressao):
    pilha = []  # Lista que vai funcionar como uma pilha

    # Percorre cada caractere na expressão
    for char in expressao:
        # Se encontrar um parêntese aberto, adiciona à pilha
        if char == '(':
            pilha.append(char)
        # Se encontrar um parêntese fechado, verifica se há parênteses abertos para fechar
        elif char == ')':
            if pilha:
                pilha.pop()  # Remove o parêntese aberto correspondente
            else:
                return False  # Se não houver parêntese aberto para fechar, a expressão está errada

    # Se a pilha estiver vazia no final, os parênteses estão balanceados
    return len(pilha) == 0


# Solicita a expressão do usuário
expressao = input('Digite uma expressão com parênteses: ')

# Verifica se os parênteses estão balanceados e mostra o resultado
if verificar_parenteses(expressao):
    print('A expressão está com os parênteses balanceados!')
else:
    print('A expressão NÃO está com os parênteses balanceados!')
