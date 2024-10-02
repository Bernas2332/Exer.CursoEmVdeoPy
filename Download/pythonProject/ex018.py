from math import sin, cos, tan, radians
n1 = float(input('Informe o valor do ângulo desejado '))
a = radians(n1)
print('O seno de {:.2f} \n é {:.2f} \n o cos é {:.2f} \n e a tg {:.2f}'.format(n1, sin(a), cos(a), tan(a)))