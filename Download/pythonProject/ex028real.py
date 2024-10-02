from random import randint
n1 = int(input('Tente acertar o número sorteado de 1 à 5 '))
n2 = randint(1, 5)
print('O número sorteado foi: {}'.format(n2))
if n1 == n2:
    print('Parabéns! você acertou')
else:
    print('Que pena! você errou')