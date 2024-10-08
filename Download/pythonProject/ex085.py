lista = []
pares = []
impares = []
for c in range(0, 7):
    n = int(input('Digite um número '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
lista.append(pares[:])
lista.append(impares[:])
print(lista)