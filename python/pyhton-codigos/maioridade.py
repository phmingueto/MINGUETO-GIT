pessoa = 1
maior = 0
menor = 0
for c in range(0, 5):
    pessoa1 = int(input("Ano de nascimento do {} aluno: ".format(pessoa)))
    pessoa = pessoa + 1
    if pessoa1 >= 2004:
        maior = maior + 1
    else:
        menor = menor + 1

print("Ao todo tivemos {} pessoas menores de idade".format(menor))
print("E também tivemos {} pessoas maiores de idade".format(maior))
