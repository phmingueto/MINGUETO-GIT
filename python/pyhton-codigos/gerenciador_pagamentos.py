valor = float(input("Valor da compra: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] À VISTA NO DINHEIRO")
print("[2] À VISTA NO CARTÃO")
print("[3] 2X NO CARTÃO")
print("[4] 3X OU MAIS NO CARTÃO")

opcao = int(input("Digite a forma de pagamento: "))

if opcao == 1:
    novo_valor = valor - (valor * 20 / 100)
    desc = (valor * 20 / 100)
    print("Sua compra será à vista no valor de R${} com desconto de R${}".format(novo_valor, desc))

elif opcao == 2:
    novo_valor = valor - (valor * 5 / 100)
    desc = valor * 5 / 100
    print("Sua compra à vista no cartão ficou no valor de R${} com desconto de R${}".format(novo_valor, desc))

elif opcao == 3:
    valor_parcela = valor / 2
    print("Sua compra em 2x de R${} ficou no valor ficou R${}".format(valor_parcela , valor))

else:
    parcela = int(input("Quantas vezes no cartão: "))
    if parcela >= 3:
        novo_valor = valor + (valor * 20 / 100)
        juros = valor * 20 / 100
        valor_parcela = novo_valor / parcela
        print("Sua compra em {}x de R${} ficou no valor de R${} com juros de R${}".format(parcela, valor_parcela, novo_valor, juros))
    else:
        print("OPÇÃO INVÁIDA!")
