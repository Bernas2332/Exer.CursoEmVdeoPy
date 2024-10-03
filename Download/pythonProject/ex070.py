n = 0
nome = 0
p = 0
c = 0
total = 0
maisb = 0
c1 = 0
while True:
    n = str(input('Digite o nome do produto '))
    p = int(input('Digite o valor do produto R$'))
    c = str(input('Deseja continuar? (S/N) ')).upper()
    c1 += 1
    if c1 <= 1:
        maisb = p
    if c == 'N':
        break
    total += p
    if p < maisb:
         maisb = p
print(maisb)
