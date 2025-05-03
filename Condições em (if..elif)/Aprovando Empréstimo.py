#vCasa = float(input('Qual o valor da casa? '))
#vSalario = float(input('Qual o valor do seu salario? '))
#anos = int (input('Quantos anos pretende pagar a casa? '))

#meses = anos*12
#prestacaoMensal = vCasa / meses
#porcenSalario = 0.3 *vSalario #Passei horas errando ate descobrir que o erro era o . ! estava colocando 0,3 inves de 0.3

#if (prestacaoMensal < porcenSalario):
#    print('Empréstimo aprovado')
#else:
#    print('Nao aprovado')


#Versao mais "arrumadinho"
vCasa = float(input('Qual o valor da casa? '))
vSalario = float(input('Qual o valor do seu salario? '))
anos = int (input('Quantos anos pretende pagar a casa? '))

prestacaoMensal = vCasa/(anos*12)
porcenSalario = 0.3 * vSalario

if (prestacaoMensal <= porcenSalario):
   print('Empréstimo aprovado')
else:
  print('Nao aprovado')


