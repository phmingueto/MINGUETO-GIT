import random
jogador = 0
pc = random.randint(1, 100)

while True:
    jogador = int(input('Diga um número: '))
    valor = input("Par ou impar [I/P]").upper()
    total = jogador + pc
    impar_par = (jogador + pc) % 2
    if impar_par == 1 and valor in 'I':
        print(f'Jogador jogou {jogador} e computador {pc} e o total deu {total} sendo um número IMPAR')
        print('Jogador Venceu!')

    elif impar_par == 0 and valor in 'P':
        print(f'Jogador jogou {jogador} e computador {pc} e o total deu {total} sendo um número PAR')
        print('Jogador Venceu!')

    else:
        print(f'Jogador jogou {jogador} e computador {pc} e o total deu {total}')
        print('Computador Venceu!')