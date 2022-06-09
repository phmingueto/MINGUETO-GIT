n = int(input("Digite um número para receber a tábuada: "))
tab = 0
c = 1

while c <= 10:
    if n < 0:
        print('Número inválido!')
        break
    tab = n * c
    print("{:2} x {:2} = {}".format(c, n, tab))
    c = c + 1
