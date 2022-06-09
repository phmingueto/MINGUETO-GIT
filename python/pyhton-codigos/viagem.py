km = float(input("Qual a distância em KM? "))

if km < 200:
    print("Deve pagar pela viagem R${}".format(km * 0.50))
else:
    print("Deve pagar pela viagem R${}".format(km * 0.45))
