nome = []
nota = []
media = []
cont = 0
while True:
    nome.append(cont)
    nome.append(str(input('Digite o nome: ')))
    nota.append(float(input('NOTA 1: ')))
    nota.append(float(input('NOTA 2: ')))
    media.append([nota[:]])

    opc = str(input('Deseja continuar? S/N'))
    cont = + 1
    if opc in 'Nn':
        break

print('RA     NOME     MÉDIA')
print(f'{nome[0]}      {nome[0]}        {media[0]}')
