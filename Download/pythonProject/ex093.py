lista = []
tudo = {}
nome = str(input('Digite o nome do jogador '))
n = int(input('Quantos jogos foram jogados pelo atleta? '))
lista.append(nome)
gols = 0
lista.append(n)
for c in range(0, n):
    gol = int(input(f'Quantos gols foram feitos na partida {c}? '))
    gols += gol
    lista.append(gol)
print(f'Nome: {nome}, gols: {lista[2:]}, total: {gols}')
tudo('nome':nome,'gols')