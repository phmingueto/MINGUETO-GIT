escola = {}

while True:
    escola['nome'] = str(input('NOME: '))
    escola['média'] = int(input('MÉDIA: '))
    break

print(f'- Nome é igual a {escola["nome"]}')
print(f'- Média é igual a {escola["média"]}')
if escola['média'] < 7:
    print('- Reprovado!')
else:
    print('- Aprovado')


