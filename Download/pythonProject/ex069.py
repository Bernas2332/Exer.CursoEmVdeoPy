s = 0
i = 0
r = 0
a = 0
b = 0
c = 0
while True:
    s = str(input('Digite o sexo (F/M) ')).upper()
    if s == 'M':
        b += 1
    i = int(input('Digite a idade '))
    if s == 'F' and i < 20:
        c += 1
    if i > 18:
        a += 1
    r = str(input('Deseja continuar? (S/N) ')).upper()
    if r != 'S':
        break
print(f'{b} pessoas são homens, {c} pessoas são mulheres com menos de 20 anos e {a} pessoas tem mais de 20 anos')