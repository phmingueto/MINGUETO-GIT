cond = "S"
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
n1 = 0

while cond in "S":
    n = int(input("Digite um número: "))
    soma = soma + n
    cont = cont + 1
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cond = input("Quer continuar? [S/N] ").upper()

print("Foram digitados {} números, tendo a média de {}".format(cont, media))
print("A soma destes números foram de {}, sendo o maior número {} e o menor {}".format(soma, maior, menor))
