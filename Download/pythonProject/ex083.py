lista = []
aberto = 0
fechado = 0
lista.append(input('Digite a sua expressão '))
for c in lista:
    if c in '(':
        aberto += 1
    if c in ')':
        fechado += 1
if fechado == aberto:
    print('Expressão válida')
else:
    print('Expressão inválida')