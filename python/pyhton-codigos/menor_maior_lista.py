lista = []
for c in range(0,7):
    lista.append(int(input(f"Digite um número na posição {c}: ")))
max = max(lista)
min = min(lista)
print(f'O maior número digitado foi {max} na posição', end=' ')
for n, c in enumerate(lista):
    if c == max:
        print(n, end='...')
print("")
print(f'O menor número digitado foi {min} na posição', end=' ')
for n, c in enumerate(lista):
    if c == min:
        print(n, end='...')