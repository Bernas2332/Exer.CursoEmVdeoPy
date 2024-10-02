n1 = int(input('Digite o ano desejado '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')