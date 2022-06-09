soma = 0
cont = 0
n = 0

while n != 999:
    n = int(input("Digite um número [999 para interromper]: "))
    soma = soma + n
    cont = cont + 1
print("A soma dos {} números digitados são {}".format(cont - 1, soma - 999))
