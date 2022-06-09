import random

print("SOU SEU COMPUTADOR..."
      "Acabei de pensar em um número de 0 a 10!"
      "Será que vocÊ consegue adivinhar?")

var = 0
cont = 0
sorteio = random.randint(0, 10)

n = int(input("Que número pensei? "))

while var == 0:
    if n < sorteio:
        print("Mais.. Tente mais uma vez!")
        n = int(input("Qual o seu palpite? "))
        cont = cont + 1

    elif n > sorteio:
        print("Menos.. Tente mais uma vez!")
        n = int(input("Qual o seu palpite? "))
        cont = cont + 1

    else:
        print("Parabéns! Você conseguiu me vencer.")
        var = 1
        cont = cont + 1

print("Você venceu na {} tentantiva!".format(cont))
