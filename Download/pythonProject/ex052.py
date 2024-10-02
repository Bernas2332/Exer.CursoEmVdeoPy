n1 = int(input('Digite um número '))
if n1 % 1 == 0 and n1 % 3 != 0 and n1 % 4 != 0 and n1 % 2 != 0:
    print('Esse número é um número primo')
else:
    print('Esse número não é um número primo')