cima = [[],[],[]]
meio = [[],[],[]]
baixo = [[],[],[]]
a = 0
b = 0
for pos in range(0,9):
    n = int(input(f'Digite um número para a posicão [{a} , {b}]: '))
    b += 1
    if b > 2:
        a += 1
        b -= 3
print(cima)