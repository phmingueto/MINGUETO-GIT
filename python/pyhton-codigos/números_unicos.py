lista = []
pos = 0
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor duplicado..')
    opc = str(input('Quer continuar? [S/N] ').upper()
    if opc in 'SN':
        print('Opção inválida!')
    if opc == 'N':
        break

print(f'Você digitou os valores {lista}')