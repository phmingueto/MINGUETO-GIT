dia = int(input("Quantos dias? "))
km = float(input("Quantos km? "))
valor_carro = dia * 60
valor_km = km * 0.15
valor_final = valor_carro + valor_km

print("Valor da locação ficou: {}".format(valor_final))

