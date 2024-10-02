from random import shuffle
n1 = input('Informe o nome de um aluno')
n2 = input('Informe o nome de um aluno')
n3 = input('Informe o nome de um aluno')
n4 = input('Informe o nome de um aluno')
lis = [n1, n2, n3 ,n4]
shuffle(lis)
print('A ordem de apresentação é')
print(lis)