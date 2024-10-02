n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
opc = 0
print(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair')
while opc != 5:
    opc = int(input('Escolha uma opção '))
    if opc == 1:
        print('A soma entre esses números é {}'.format(n1+n2))
    if opc == 2:
        print('A multiplicação entre esses números é {}'.format(n1*n2))
    if opc == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if opc == 4:
        n1 = int(input('Digite um número '))
        n2 = int(input('Digite outro número '))
print ('FIM')