soma = 0
for c in range(0, 7):
    n = int(input('Digite um número '))
    if n % 2 == 0:
        soma = soma + n
print('Entre os números pares que você digitou, a soma deles é {}'.format(soma))
