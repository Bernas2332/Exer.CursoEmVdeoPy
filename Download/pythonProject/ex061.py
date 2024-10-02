n1 = int(input('Digite o valor inicial de sua PA '))
n2 = int(input('Digite a razão de sua PA '))
pa = 0
while pa < n2*9:
    pa += n2
    print(n1 + pa)