def maior_elemento(lista):
  max_lista = lista[0]
  for valor in lista:
    if max_lista < valor:
      max_lista = int(valor)
  return max_lista

print(maior_elemento([1, 2, 3, 4, 10,35,10]))
