from random import randint
from time import sleep
resultados = {}
for c in range(0, 4):
    resultados['valor'] = randint(0,6)
    print(f'O jogador número {c} tirou {resultados['valor']}')
    