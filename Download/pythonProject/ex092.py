lista = {}
lista['nome'] = str(input('Digite seu nome '))
lista['nascimento'] = int(input('Digite seu ano de nascimento '))
lista['carteira de trabalho'] = int(input('Digite sua carteira de trabalho (digite 0 caso não tenha '))
lista['contratação'] = int(input('Digite o seu ano de contratação '))
lista['salário'] = int(input('Digite o seu salário R$'))
print(lista)
for c, i in lista:
    print(f'{lista} tem o valor {}')