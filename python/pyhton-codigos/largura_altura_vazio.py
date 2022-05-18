altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))

i = 0
while i < largura:
    j = 0
    while j < altura:
        if i == 0 or i == largura-1 or j == 0 or j == altura-1:
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        j += 1
    print()
    i += 1
