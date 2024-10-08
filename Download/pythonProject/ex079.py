lista = []
n = 0
while True:
    n = int(input('Digite um número '))
    if n not in lista:
        lista.append(n)
    else:
        print('Esse valor já existe na lista')
    r = str(input('Deseja continuar? (S/N)'))
    if r in 'Nn':
        break
print(lista)
