n1 = float(input('Digite um número '))
n2 = float(input('Digite outro número '))
n3 = float(input('Digite outro número '))
n4 = float(input('Digite o último número '))
lista = (n1, n2, n3, n4)
nove = 0
if n1 == 9:
    nove += 1
if n2 == 9:
    nove += 1
if n3 == 9:
    nove += 1
if n4 == 9:
    nove += 1
tres = 0
print(f'O número nove aparece {nove} vezes.')
if 3 in lista:
    print(f'O primeiro número 3 foi digitado na posição {lista.index(3)+1}')
print('Os números pares nessa lista são:',end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
