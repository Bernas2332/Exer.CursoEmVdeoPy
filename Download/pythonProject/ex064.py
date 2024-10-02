n = 0
c = 0
c2 = 0
c0 = 0
while n+c != 999:
    c = int(input('Digite um número, 999 se quiser parar '))
    c2 += c
    c0 += 1
print('Dos {} números digitados, a soma entre eles é igual à {}'.format(c0-1, c2-999))