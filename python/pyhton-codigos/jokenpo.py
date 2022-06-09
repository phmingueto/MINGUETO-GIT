import random
from time import sleep

print("SUAS OPÇÕES:")
print("[1] PEDRA")
print("[2] PAPEL")
print("[3] TESOURA")

opcao = int(input("Escolha uma opcão: "))

lista = ["PEDRA", "PAPEL", "TESOURA"]
maquina = random.randint(1, 3)

print("JO")
sleep(1)
print("kEN")
sleep(1)
print("PO!!")
sleep(1)

print("-=-" * 5)

print("Jogador jogou {}".format(lista[opcao - 1]))
print("Maquina jogou {}".format(lista[maquina - 1]))

print("-=-" * 5)
sleep(2)

if opcao == 1 and maquina == 2:
    print("MAQUINA VENCEU!")

elif opcao == 1 and maquina == 3:
    print("JOGADOR VENCEU!")

elif opcao == 2 and maquina == 3:
    print("MAQUINA VENCEU")

elif opcao == 2 and maquina == 1:
    print("JOGADOR VENCEU")

elif opcao == 3 and maquina == 1:
    print("MAQUINA VENCEU")

elif opcao == 3 and maquina == 2:
    print("MAQUINA VENCEU")

else:
    print("EMPATOU")
