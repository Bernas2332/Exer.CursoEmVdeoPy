n1 = int(input('Digite o termo inicial de sua PA '))
n2 = int(input('Digite a razão de sua PA '))
c = 1
pa = 1
n = 0
while pa != 0 and n < 10 and c == c:
    n += 1
    pa = n2
    print(n1+pa*n)
    if n == 10:
        while c != 0:
            c = int(input('pausa, se desejar continuar, digite um número para ser a quantidade de vezes que a PA continuará '))
            while n2 != c:
                n2 += 1
                print(n1*pa*n2)