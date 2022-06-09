valor = int(input("Qual valor quer sacar? "))

ciquenta = valor // 50
ciquenta_r = valor % 50
vinte = ciquenta_r // 20
vinte_r = ciquenta_r % 20
dez = vinte_r // 10
dez_r = vinte_r % 10
um = dez_r // 1

if ciquenta != 0:
    print(f'Total de {ciquenta} cédulas de R$ 50')
if vinte != 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez != 0:
    print(f'Total de {dez} cédulas de R$10')
if um != 0:
    print(f'Total de {um} cédulas de R$1')