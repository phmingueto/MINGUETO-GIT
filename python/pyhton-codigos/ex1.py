
número = int(input("digite um número para saber se é par ou impar: "))
resultado = número % 2

if resultado == 0:
    print("o número", número, "é PAR")
else:
    print("o número", número, "é IMPAR")
