soma = int(input("Digite um número: "))

soma10 = soma % 10
soma100 = soma % 100
soma1000 = soma % 1000

soma_total = soma10 + soma100 + soma1000

print(soma_total)
