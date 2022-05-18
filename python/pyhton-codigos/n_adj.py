n = int(input("Digite um número: "))

anterior = n % 10
n = n // 10
n_adj = False
pos = 0

while n > 0 and not n_adj:
    atual = n % 10
    if atual == anterior:
        n_adj = True

    else:
        pos = pos + 1
    anterior= atual
    n = n // 10


if n_adj:
    print("sim")

else:
    print("não")
    
