velocidade = float(input("Qual velocidade você passou pelo radar? "))

if velocidade > 80:
    print("Você foi multado!")
    print("Deve pagar uma multa de R${}".format((velocidade - 80) * 7))
else:
    print("Não fou multado!")
