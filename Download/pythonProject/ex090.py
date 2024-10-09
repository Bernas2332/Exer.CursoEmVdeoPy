lista = {}
lista['nome'] = str(input('Digite o nome do aluno '))
lista['média'] = float(input('Digite a média desse aluno '))
print(lista)
if lista['média'] >= 7:
    print('Esse aluno(a) foi aprovado')
else:
    print('Esse aluno(a) foi reprovado')