n = int(input('Quantos números você quer ver da sequência de fibonacci? '))
n1 = 0
n2 = 1
c = 3
print('{} - {}'.format(n1,n2),end=' - ')
while c <= n:
    n3 = n1 + n2
    print('{}'.format(n3),end=' - ')
    n1 = n2
    n2 = n3
    c += 1
print('fim')