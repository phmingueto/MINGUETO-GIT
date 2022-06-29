pessoas = {}
lista = []
nome_mulher = []
opc = 'a'
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('NOME: '))
    pessoas['sexo'] = str(input('SEXO: '))
    pessoas['idade'] = int(input('IDADE: '))
    lista.append(pessoas.copy())
    opc = input('Deseja continuar? [S/N]')
    if opc in 'NnSs':
        if opc in 'Nn':
            break
        elif opc in 'Ss':
            print('Continuando...')

    else:
        print('OPÇÃO ERRADA!')

print(f'A) Ao todo temos {len(lista)} cadastradas.')

for c in lista:
    media = media + c['idade']
media = media / len(lista)
print(f'A média das idades foram de {media} anos')

print(f'As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] in 'Ff':
        print(c['nome'])

print('Pessoas cadastradas que estão acima da média:', end='')
for c in lista:
    if c['idade'] > media:
        print(f'nome = {c["nome"]}; idade = {c["idade"]}; sexo = {c["sexo"]}')


