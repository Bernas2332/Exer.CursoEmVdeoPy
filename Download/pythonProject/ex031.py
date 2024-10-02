n1 = float(input('Digite a distância da viagem em km '))
if n1 <= 200:
    print('O custo dessa viagem será de R${}'.format(n1*0.50))
else:
    print('O custo dessa viagem será de R${}'.format(n1*0.45))
