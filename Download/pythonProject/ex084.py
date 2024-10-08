pessoas = []
while True:
    pessoas.append(str(input('Digite o nome da pessoa ')))
    pessoas.append(int(input('Digite o peso dessa pessoa ')))
    r = str(input('Deseja continuar? (S/N) '))
    if r in 'Nn':
        break
print(f'Foram adicionados {len(pessoas)/2:.0f} pessoas nessa lista ')