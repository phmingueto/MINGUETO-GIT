from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10),  randint(1, 10))

print('Os números sorteados foram: ', end=' ')

for c in n:
    print(f'{c}', end=' ')

print("")
print(f'O menor número é: {min(n)}')
print(f'O maior número é: {max(n)}')

