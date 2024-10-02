n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mVocê foi reprovado.')
elif m >= 5 and m < 6.9:
    print('\033[33mVocê está de recuperação')
elif m >= 7:
    print('\033[32mVocê foi aprovado.')