def ficha(n='desconhecido', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato')


n = str(input('Digite o nome do jogador '))
g = int(input('Digite quantos gols ele fez '))
ficha(n, g)