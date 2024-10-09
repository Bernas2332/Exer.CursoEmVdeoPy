from time import sleep
def contagem(a, b, c):
    for c in range(a, b, c):
        print(c, end=' ')
       


contagem(1, 11, 1)
contagem(10, -1, -2)
print('Contagem personalizada, decida seu:')
a = int(input('Ínicio '))
b = int(input('Fim '))
if b > 0:
    b += 1
else:
    b -= 1
c = int(input('De quanto em quanto? '))
contagem(a,b,c)