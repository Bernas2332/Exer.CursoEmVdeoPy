lista = ('Caneta', 'R$2,50', 'Lápis', 'R$1,00', 'Borracha', 'R$0,50', 'Estojo', 'R$10,00')
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:-<30}',end='')
    else:
        print(f'{lista[n]}')