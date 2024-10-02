n = 0
p = 0
t = 0
mb = 0
s = 0
a = 0
while True:
    n = str(input('Digite o nome do produto '))
    p = p2
    p2 = float(input('Digite o valor do produto R$'))
    if p2 > 1000:
        a += 1
    t += p
    if p < p2:
        mb = p
    s = str(input('Deseja continuar? (S/N) ')).upper()
    print(mb)
    if 'N' in s:
        break
print(f'O total foi R${t}, com {a} produtos custando mais que R$1000 e o mais barato sendo {} por R${}')