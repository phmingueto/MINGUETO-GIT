pessoa = 1
maior = 0
menor = 1000

for c in range(0, 5):
    peso = float(input("Qual o peso do aluno {} aluno: ".format(c)))
    pessoa = pessoa + 1
    peso1 = peso
    if peso > maior:
        maior = peso
        if peso1 < menor:
            menor = peso1

print("Maior peso é {}".format(maior))
print("Menor peso é {}".format(menor))
