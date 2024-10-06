lista = []
maior = 0
menor = 0
for num in range(0,5):
    lista.append(int(input('Digite um número ')))
    if num == 0:
        maior = menor = lista[num]
    else:
        if maior < lista[num]:
            maior = lista[num]
        if menor > lista[num]:
            menor = lista[num]
print(f'O maior é {maior} e o menor {menor}')