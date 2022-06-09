palavra = ('APRENDER', 'JULGAR', 'MELHORAS', 'LUTAR', 'VEGETAR')
vogal = ('A', 'E', 'I', 'O', 'U')


for p in palavra:
    pos = 0
    n1 = len(p)
    print(f'Na palavra {p} temos', end = ' ')
    while pos != n1:
        if p[pos] in vogal:
            print(p[pos], end =' ')
        pos = pos + 1
    print('')