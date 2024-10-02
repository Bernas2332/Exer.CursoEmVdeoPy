from math import pow
c1 = float(input('Digite o comprimento do cateto oposto'))
c2 = float(input('Digite o comprimento do cateto adjacente'))
c1a = pow(c1, 2)
c2a = pow(c2, 2)
c = c1a+c2a
h = pow(c, 0.5)
print('A hipotenusa desse triângulo é {:.1f}'.format(h))