from datetime import datetime

# Criando o dicionário
pessoa = {}

# Entrada de dados
pessoa['nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc  # calculando a idade atual
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    
    # Calculando aposentadoria → 35 anos de contribuição
    anos_trabalhados = datetime.now().year - pessoa['contratacao']
    tempo_restante = 35 - anos_trabalhados
    pessoa['aposentadoria'] = pessoa['idade'] + tempo_restante

# Mostrando os dados
print('\n--- Cadastro completo ---')
for k, v in pessoa.items():
    print(f'{k}: {v}')
