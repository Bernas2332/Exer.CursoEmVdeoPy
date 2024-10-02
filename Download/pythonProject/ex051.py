soma = 0
n1 = int(input('Digite o primeiro termo de sua PA '))
n2 = int(input('Digite a razão desejada '))
n3 = n1 + (10-1) * n2
for c in range(n1, n3, n2):
    print('{}'.format(c), end=' - ')
print('FIM')