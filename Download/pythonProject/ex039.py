from datetime import date
n2 = int(input('Informe o ano em que nasceu '))
n3 = 2024
n1 = n3 - n2
if n1 > 18:
    print('Parece que a sua época de alistamento ja passou faz {} anos'.format(n1-18))
elif n1 < 18:
    print('Parece que a sua época de alistamento ainda não chegou, espere mais {} anos'.format(18-n1))
else:
    print('Parece que agora é a sua hora! esse ano você deve se alistar.')
