n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))
if n1 > n2:
    print('{} é o maior número'.format(n1))
elif n2 > n1:
    print('{} é o maior número'.format(n2))
else:
    print('Não há um número maior.')
