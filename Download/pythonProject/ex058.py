from random import randint
ten = 0
c = randint(1, 10)
n = 1
t = 0
while c != n:
    t += 1
    n = int(input('Tente adivinhar o número que estou pensando, de 1 até 10 '))
    if n == c:
        print('\033[32m Parabéns, você acertou o número\033[m')
    else:
        print('\033[33m Que pena, tente novamente\033[m ')
print('Te levaram {} tentativas para acertar!'.format(t))