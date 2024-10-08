lista = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um número '))
    r = str(input('Deseja continuar? (S/N) '))
    if r in 'Nn':
        break
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
    lista.append(n)
print(f'Os números que você digitou são: {lista}')
print(f'Os números pares que você digitou são {lista2}')
print(f'Os números ímpares que você digitou são {lista3}')