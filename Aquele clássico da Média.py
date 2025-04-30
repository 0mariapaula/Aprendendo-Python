n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print('Sua média é {:.2f} e você foi aprovado'.format(media))
elif media < 5:
    print('Sua média é {:.2f} e você foi reprovado'.format(media))
else:
    print('Sua média é {:.2f} e você está de recuperação'.format(media))
