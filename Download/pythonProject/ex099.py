def maior(*num):
    cont = maior = 0
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor é {maior}')


maior(1,2,3,5,8,3, 23)