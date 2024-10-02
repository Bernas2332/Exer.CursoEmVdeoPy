n1 = float(input('Digite o valor do salário R$' ))
if n1 < 1250:
    print('O seu novo salário será de R${}'.format(n1*1.15))
else:
    print('O seu novo salário será de R${}'.format(n1*1.10))