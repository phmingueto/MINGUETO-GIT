import random
print("Vou penser em um número entre 0 e 5. Tente adivinhar...")
var = 0
sorteio = random.randint(0, 5)

while var == 0:
   n = int(input("Que número pensei? "))

   if sorteio == n:
       print("Parabéns! Você conseguiu me vencer.")
       var = 1
   else:
       print("Ops, continue tentando!")
