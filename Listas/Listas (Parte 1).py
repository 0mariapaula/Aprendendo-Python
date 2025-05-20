#APPEND()
frutas = ['maçã', 'banana']
print('Antes do append:', frutas)

frutas.append('uva')  # Adiciona 'uva' no final
print('Depois do append:', frutas)

#INSERT()
frutas = ['maçã', 'banana', 'uva']
print('Antes do insert:', frutas)

frutas.insert(1, 'abacaxi')  # Adiciona 'abacaxi' na posição 1
print('Depois do insert:', frutas)

#_____________________________________________________
#REMOVE(VALOR)
numeros = [10, 20, 30, 40]
print('Antes do remove:', numeros)

numeros.remove(30)  # Remove o número 30
print('Depois do remove:', numeros)

#POP()
numeros = [10, 20, 30, 40]
print('Antes do pop:', numeros)

ultimo = numeros.pop()  # Remove o último (40)
print('Depois do pop:', numeros)
print('Valor removido:', ultimo)

#POP(POSIÇÃO)
numeros = [10, 20, 30, 40]
print('Antes do pop(1):', numeros)

removido = numeros.pop(1)  # Remove o número na posição 1 (20)
print('Depois do pop(1):', numeros)
print('Valor removido:', removido)

#_____________________________________________________
#ALTERAR[]
numeros = [10, 20, 30, 40]
print('Antes da troca:', numeros)

numeros[1] = 99  # Troca o valor da posição 1 (20) por 99

print('Depois da troca:', numeros)
