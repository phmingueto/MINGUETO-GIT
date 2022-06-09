ex = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
      'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ')

n = int(input('Digite um número de 0 a 10: '))

if 0 <= n <= 10:
    print(f'O número digitado é {ex[n]}')
else:
    print('Opção inválida!')

