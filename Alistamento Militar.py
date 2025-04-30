from datetime import date

nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year #year = ANO
idade = ano_atual - nascimento

print()
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano_atual))

if idade < 18:
    falta = 18 - idade
    print('Você ainda vai se alistar ao serviço militar.')
    print('Faltam {} ano(s) para o alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(ano_atual + falta))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    passou = idade - 18
    print('Você já deveria ter se alistado.')
    print('Você está atrasado há {} ano(s).'.format(passou))
    print('Seu alistamento foi em {}.'.format(ano_atual - passou))
