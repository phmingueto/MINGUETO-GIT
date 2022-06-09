from operator import itemgetter
import random
ranking = {}
jogador = {'1º Jogador': random.randint(1, 7), '2º Jogador': random.randint(1, 7),
           '3º Jogador': random.randint(1, 7), '4º Jogador': random.randint(1, 7)}

for k, v in jogador.items():
    print(f'{k} tirou {v} no dado')

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i, v in enumerate(ranking):
    print(f'{v[0]} ficou em {i + 1} lugar pois tirou {v[1]}')


