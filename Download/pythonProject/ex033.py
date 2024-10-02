n1 = float(input('Digite um número '))
n2 = float(input('Digite um número '))
n3 = float(input('Digite um número '))
m = n1
if n2<n1 and n2<n3:
    m = n2
if n3<n1 and n3<n2:
    m = n3
ma= n1
if n2>n1 and n2>n3:
    ma = n2
if n3>n1 and n3>n2:
    ma = n3
print('O menor número é {:.0f} e o maior é {:.0f}'.format(m, ma))
