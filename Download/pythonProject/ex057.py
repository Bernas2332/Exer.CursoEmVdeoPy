s = 0
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo (M/F) ')).upper().strip()[0]
    if s == 'M':
        print('Sexo selecionado: masculino ')
    if s == 'F':
        print('Sexo selecionado: feminino')
    else:
        print('Digite novamente')