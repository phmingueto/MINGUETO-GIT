emprestimo = float(input("Qual o valor do empréstimo? R$: "))
salario = float(input("Qual o valor do seu salário? R$: "))
anos = int(input("Em quantos anos pretende parcelar o empréstimo? "))

parcela = emprestimo / (anos * 12)
min = parcela * 30 / 100


print("Para pagar o empréstimo de {:.2f} em {:.2f} anos a prestação será de R${:.2f}".format(emprestimo, anos, parcela))

if parcela <= min:
    print("Empréstimo CONCEDIDO!")

else:
    print("Empréstimo NEGADO!")
