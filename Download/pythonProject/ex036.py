print('Olá, iremos checar se o seu empréstimo será aprovado.')
n1 = float(input('Informe o valor da casa: R$'))
n2 = float(input('Informe o salário do comprador: R$'))
n3 = float(input('Informe em quantos anos será pago '))
n = n1 / (n3 * 12)
if n < n2 * 0.30:
    print('\033[31mLamento, seu empréstimo foi negado')
else:
    print('\033[0;32mTudo certo, seu empréstimo foi aprovado!\n serão {} prestações de {}'.format(n3*12, n))
