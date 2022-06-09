totmulher = 0
p = 0
h = 0

while True:
    idade = int(input("IDADE: "))
    sexo = input("SEXO (M/F): ").upper().strip()
    opcao = input('Deseja continuar [S/N]? ').upper().strip()

    if opcao == 'N':
        print('Terminamos por aqui!')
        break

    elif opcao in 'S':
        if idade >= 18:
            p = p + 1
        if idade <= 20 and 'F' in sexo:
            totmulher = totmulher + 1
        if 'M' in sexo:
            h = h + 1


print("No grupo exitem {} mulheres menores de 20 anos.".format(totmulher))
print("No grupo exitem {} homens cadastrados".format(h))
print("No grupo exitem {} pessoas maiores de 18 anos cadastrados".format(p))