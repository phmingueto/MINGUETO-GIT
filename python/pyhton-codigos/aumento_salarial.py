salario = float(input("Digite seu salário para saber a alteração: R$"))
if salario < 1250:
    print("Seu salário de R${} foi para R${}". format(salario, ((salario * 15 / 100) + salario)))
else:
    print("Seu salário de R${} foi para R${}".format(salario, ((salario * 10 / 100) + salario)))
