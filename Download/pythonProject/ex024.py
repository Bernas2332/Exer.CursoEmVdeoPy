n = int(input('Digite um número de 0 à 9999 '))
u = n / 1 % 10
d = n /10 % 10
c = n / 100 % 10
m = n / 1000 % 10
print('Nesse número, sua \n  unidade é {:.0f} \n a dezena é {:.0f} \n a centena {:.0f} \n o milhar {:.0f}'.format(u, d, c, m))
