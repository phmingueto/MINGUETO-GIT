altura = float(input("Qual altura? "))
largura = float(input("Qual largura? "))
área = altura * largura

print("Sua parede tem a dimensão de {} X {} e sua área é de {}m²".format(altura, largura, área))
print("Para pintar está parede você precisará de {}L de tinta".format(área/2))