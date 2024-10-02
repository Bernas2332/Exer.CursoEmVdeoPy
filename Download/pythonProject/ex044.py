n1 = float(input('Digite o valor do produto R$'))
a = str(input('Informe o meio de pagamento (aceitamos: cartão, cheque e dinheiro'))
n2 = int(input('Caso tenha selecionado cartão, em quantas vezes gostaria de parcelar? '))
a1 = a.lower().strip()
if 'cartão' in a1 and n2 == 2:
    print('Com essas combinações de pagamento, você pagará o preço normal!')
elif 'cartão' in a1 and n2 >= 3:
    print('Com essas combinações de pagamento, você pagará com 20% de juros, que deixaria o valor total em {}'.format(n1*0.20*n2))
elif 'cartão' in a1 and n2 == 1:
    print('Com essas combinações de pagamento, você pagará com 5% de desconto, o que seria {}'.format(n1*0.95))
elif 'dinheiro' in a1 or 'cheque' in a1:
    print('Com essas combinações de pagamento, você pagará com 20% de desconto, que seria {}'.format(n1*0.80))