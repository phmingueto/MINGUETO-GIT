futebol = {}
gol = []
futebol['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou? '))

for p in range(1, partidas + 1):
    gol.append(int(input(f"Quantos gols na partida {p}?" )))
futebol['gols'] = gol[:]
futebol['total'] = sum(gol)

print(futebol)

for k, v in futebol.items():
    print(f'O {k} tem o valor de {v}')

print(f'O jogador {futebol["nome"]} jogou {partidas} partidas')
for i, v in enumerate(gol):
    print(f'Na partida {i + 1} ele fez {v}')
print(f'Total de {futebol["total"]} gols!')
