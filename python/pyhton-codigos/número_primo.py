n = int(input("Digite um número: "))
cont = 0
for c in range(1, n + 1):
    if n % c == 0 and n % n == 0:
       cont = cont + 1
if cont == 2 and n != 1:
    print("PRIMO")
else:
    print("NÃO PRIMO")