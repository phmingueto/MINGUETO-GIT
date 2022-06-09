valor = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        valor = c + valor
        cont = cont + 1
print(cont)
print(valor)



