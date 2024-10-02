from opcode import cmp_op

n1 = float(input('Digite o valor em metros '))
k = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
print('{}m é igual à \n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(n1, k, hm, dam, dm, cm, mm))

