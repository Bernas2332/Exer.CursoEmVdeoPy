n = int(input('Digite um número para saber seu fatorial '))
n2 = n
n3 = 1
while n2>0:
    n3 *= n2
    n2 -= 1
print(n3)