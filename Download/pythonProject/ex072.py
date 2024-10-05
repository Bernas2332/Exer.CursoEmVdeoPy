números = ('zero',  'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dessoito', 'dessenove', 'vinte')
n = int(input('Digite um número de 0 à 20: '))
while n < 0 or n > 20:
    n = int(input('Oops, tente novamente, digite um número de 0 à 20: '))
print(f'{n} por extenso é {números[n]}')