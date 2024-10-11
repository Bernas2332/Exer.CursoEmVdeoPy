notas = {}
notas['maior'] = 234

def notas(x):
    r = 0
    while True:
        x = int(input('Digite a nota desejada '))
        r = str(input('Deseja adicionar mais uma nota? '))
        if r in 'nN':
            break
