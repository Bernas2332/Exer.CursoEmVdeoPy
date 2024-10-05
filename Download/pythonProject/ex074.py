from random import randint
lista = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
menor = lista[0]
if menor > lista[1]:
    menor = lista[1]
elif menor > lista[2]:
    menor = lista[2]
elif menor > lista[3]:
    menor = lista[3]
elif menor > lista[4]:
    menor = lista[4]
elif menor > lista[5]:
    menor = lista[5]
maior = lista[0]
if maior < lista[1]:
    maior = lista[1]
elif maior < lista[2]:
    maior = lista[2]
elif maior < lista[3]:
    maior = lista[3]
elif maior < lista[4]:
    maior = lista[4]
elif maior < lista[5]:
    maior = lista[5]
print(lista)
print(f'O menor número dessa lista é {menor} e o maior {maior}')