n = int(input("Digite um número inteiro terminado com zero: "))

lista_numero = []

while n != 0:
       lista_numero.append(n)
       n = int(input("Digite um número inteiro terminado com zero: "))
       
lista_numero.sort()
print(lista_numero)

    
