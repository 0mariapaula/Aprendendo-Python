def ajuda(comando):
    cor = '\033[1;36m'  # azul claro
    fim = '\033[m'
    print(f'{cor}', end='')
    help(comando)
    print(fim, end='')

while True:
    print('\033[1;32m' + '-'*30)
    comando = input('Função ou Biblioteca > ').strip()
    if comando.upper() == 'FIM':
        print('\033[1;31mEncerrando o sistema... Até logo!\033[m')
        break
    ajuda(comando)