n1 = int(input('Digite o ano de nascimento do atleta '))
n = 2024 - n1
if n <= 9:
    print('atleta: MIRIM')
elif n <= 14:
    print('atleta: INFANTIL')
elif n <= 19:
    print('atleta: JUNIOR')
elif n <= 20:
    print('atleta: SÊNIOR')
else:
    print('atleta: MASTER')