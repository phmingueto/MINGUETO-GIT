import random
random.seed()
lista = []
v = int(input("Quantos jogos da Mega Sena você precisa? "))

for j in range(1, v + 1):
    for p in range(1, 7):
        n = random.randint(1, 61)
        lista.append(n)
        lista.sort()
    print(f'Jogo {j}: {lista}')
    lista.clear()

