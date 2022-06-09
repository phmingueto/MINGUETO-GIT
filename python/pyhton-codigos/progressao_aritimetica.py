primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

for c in range(primeiro_termo, 10, razao):
    print(c, "-->" , end="")
print("ACABOU")