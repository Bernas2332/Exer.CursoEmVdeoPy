l1 = float(input('Digite o valor da primeira linha '))
l2 = float(input('Digite o valor da segunda linha '))
l3 = float(input('Digite o valor da terceira linha '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l2 > l1:
    print('Essas linhas juntas, formam um triângulo.')
    if l1 == l2 == l3:
        print('Que por sua vez, é EQUILÁTERO')
    elif l1 != l2 != l3 and l1 != l3:
        print('Que por sua vez é ESCALENO')
    else:
        print('Que por sua vez, é ISÓSCELES')
else:
    print('Essas linhas juntas, não formam um triângulo')
