from random import randint
print('Olá, vamos jogar um jogo de pedra papel e tesoura')
n1 = str(input('Informe qual será a sua jogada '))
a = randint(1, 3)
n1a = n1.lower().strip()
v = '\033[32mParabéns, dessa vez, você ganhou'
e = '\033[33mOops, parece que foi um empate'
d = '\033[31mQue pena! dessa vez, eu ganhei'
if 'pedra' in n1a and a == 1:
    print(e)
elif 'pedra' in n1a and a == 2:
    print(v)
elif 'pedra' in n1a and a == 3:
    print(d)
elif 'papel' in n1a and a == 1:
    print(v)
elif 'papel' in n1a and a == 2:
    print(e)
elif 'papel' in n1a and a == 3:
    print(d)
elif 'tesoura' in n1a and a == 1:
    print(d)
elif 'tesoura' in n1a and a == 2:
    print(v)
elif 'tesoura' in n1a and a == 3:
    print(e)
else:
    print('Parece que você digitou algo errado!')