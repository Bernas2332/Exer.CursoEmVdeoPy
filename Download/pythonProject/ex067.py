n = 0
c = 1
while True:
    n = int(input('Digite um número '))
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n*c}')
    c = 1
print('fim')