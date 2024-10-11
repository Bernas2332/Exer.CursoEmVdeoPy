def éint(n=0):
    while True:
        n = input('Digite um número ')
        if n.isnumeric():
            print(f'O valor {n} é um número')
            break
        else:
            print('\033[31m Erro! digite um número.\033[m')



éint()