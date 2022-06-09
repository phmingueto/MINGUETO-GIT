inser = input("Digite uma frase: ").strip().upper()
palavras = inser.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]

if inverso == junto:
    print(" A frase {} e {} são Palíndromo!".format(junto, inverso))
else:
    print(" A frase {} e {} não são Palíndromo!".format(junto, inverso))


