x = 100
maior = 0

while x != 10:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")

    x = int(input("Qual sua opção? "))

    if x == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    if x == 2:
        multiplo = n1 * n2
        print("A mutiplicação entre {} e {} é {}".format(n1, n2, multiplo))
    if x == 3:
        if n1 > n2:
            maior = n1
            print("O maior entre {} e {} é {}".format(n1, n2, maior))
        else:
            maior = n2
            print("O maior entre {} e {} é {}".format(n1, n2, maior))
    if x == 4:
        print("Escolha novos números!")
    if x == 5:
        print("FIM DO PROGRAMA, VOLTE SEMPRE!")
        x = 10
