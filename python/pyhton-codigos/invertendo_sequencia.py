n = int(input("Digite um número ou 0 para encerrar: "))
lista = []
pos = 0
x = 1
while x != 0:
    if n != 0:
        lista.append(n)
        n = int(input("Digite um número ou 0 para encerrar: "))

    else:
        while len(lista) > pos:
            print(lista[0 + pos])
            pos = pos + 1

x = 0


