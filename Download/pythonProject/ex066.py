n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um número (999 para parar) '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma desses números é igual à {s} e {c} foram digitados')