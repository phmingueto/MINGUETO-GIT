trabalho = {}

trabalho['nome'] = str(input('NOME: '))
trabalho['ano'] = int(input('Ano de Nascimento: '))
idade = 2022 - trabalho['ano']
trabalho['ctps'] = int(input('Número da Carteira de Trabalho [0 caso não possua]: '))

if trabalho['ctps'] == 0:
    print(f'- Nome tem o valor de {trabalho["nome"]}')
    print(f'- Ano de nascimento tem o valor de {trabalho["ano"]}, portando tem {idade} anos')
    print(f'- Carteira de Trabalho não tem valor')

else:
    trabalho['contratação'] = int(input('Ano de Contratação: '))
    trabalho['salário'] = int(input('Salário R$: '))
    contrato = 65 - (2022 - trabalho['contratação'])
    print(f'- Nome tem o valor de {trabalho["nome"]}')
    print(f'- Ano de nascimento tem o valor de {trabalho["ano"]}, portando tem {idade} anos')
    print(f'- Ano de contratação tem o valor de {trabalho["contratação"]}, provavel aposentadoria daqui {contrato} anos')
    print(f'- Salário tem o valor de R${trabalho["salário"]}')