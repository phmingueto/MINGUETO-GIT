ano = int(input("Digite o ano de nascimento: "))
idade = 2022 - ano
alistamento = ano + 18
print("Quem nasceu em {} tem {} anos em 2022".format(ano, idade))

if idade == 18:
    print("Você precisa se alistar IMEDIATAMENTE!")

elif idade > 18:
    print("Seu ano de alistamento foi em {}".format(alistamento))

elif idade < 18:
    print("Você precisa se alistar em {}". format(alistamento))
    print("Ainda faltam {} anos".format(alistamento - 2022 ))