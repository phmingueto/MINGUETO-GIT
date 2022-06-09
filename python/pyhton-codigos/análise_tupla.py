cont = 0
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
d = int(input("Digite um número: "))

tupla = (a, b, c, d)

print(f'Você digitou os números {tupla}')
print(f' O valor {a} apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f' O valor {3} apareceu na {tupla.index(3) + 1}° posição')
else:
    print('Número 3 não digitado')

print(f'Os números pares são:', end= ' ')

for c in tupla:
    if c % 2 == 0:
        print(c, end= ' ')




