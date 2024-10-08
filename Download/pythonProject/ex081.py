c = 0
lista = []
while True:
    lista.append(int(input('Digite um numero ')))
    r = str(input('Gostaria de continuar? (S/N) '))
    if r in 'nN':
        break
print(f'A quantidade de valores digitados foi {len(lista)}')
lista.sort(reverse= True)
print(f'A sua lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está presente em sua lista')
else:
    print('O número 5 não está presente na sua lsita')