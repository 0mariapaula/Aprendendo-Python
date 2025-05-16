# Crie um programa que tenha uma tupla com várias
# palavras (não usar acentos). Depois disso, você deve mostrar, para cada
# palavra, quais são as suas vogais.

palavras = (
    'python', 'curso', 'gratis', 'estudar', 'programar',
    'desenvolver', 'teclado', 'aprender', 'computador', 'internet'
)

vogais = 'aeiou'

for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos:', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
