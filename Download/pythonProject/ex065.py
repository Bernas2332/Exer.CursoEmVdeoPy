n = 0
r = 'S'
c = 0
s = 0
maior = 0
menor = 99999
while 'S' in r:
    n = int(input('Digite um número '))
    r = str(input('Deseja continuar ?(S/N) ')).upper().strip()
    c += 1
    s += n
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
m = s / c
print('Você digitou {} números, e a média deles é {} '.format(c, m))
print('E, o maior deles é {} e o menor {}'.format(maior, menor))

