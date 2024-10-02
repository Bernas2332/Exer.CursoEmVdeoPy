from random import randint
n = 0
r = 0
n1 = randint(0, 10)
p = 'P'
i = 'I'
v = 0
n0 = 0
r1 = 0
while True:
    n = int(input('Digite um número '))
    n1 = randint(0, 10)
    n0 = n
    n += n1
    n2 = n
    r = str(input('Par ou ímpar? (P/I) ')).upper()
    if r == i:
        r = i
    if r == p:
        r = p
    if n % 2 == 0:
        r1 = p
    else:
        r1 = i
    if r == r1:
        print(f'A máquina digitou {n1} e você {n0}, que a soma é {n2}, logo, você venceu')
        v += 1
    if r != r1:
        print(f'A máquina digitou {n1} e você {n0}, que a soma é {n2}, logo, você perdeu')
        break
print(f'Fim de jogo, você venceu {v} vezes ')


