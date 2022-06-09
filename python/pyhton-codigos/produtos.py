nome = ''
total = 0
maior = 0
cont = 0
menor = 0
nome_b = ''
c = 0
while True:
    nome = input("Nome do produto: ")
    valor = float(input("Preço do produto: "))
    total = total + valor
    c = c + 1
    if c == 1 or valor < menor:
        menor = valor
        nome_b = nome
    if valor > 1000:
        cont = cont + 1
    opcao = input("Deseja continuar? [S/N]: ").upper()
    if opcao in 'N':
        break

print(f'O total da compra foi de R${total}')
print(f'Tiveram {cont} produtos com valores acima de R$1000')
print(f'O {nome_b} é o produto de menor valor custando R${menor}')