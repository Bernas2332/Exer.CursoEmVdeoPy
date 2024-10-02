n1 = float(input('Digite a velocidade do carro (em km/h) '))
if n1 <= 80:
    print('Esse carro não excedeu o limite de velocidade')
else:
    print('AVISO! velocidade excedida por {}km/h, a multa será de R${}'.format(n1-80, (n1-80)*7))