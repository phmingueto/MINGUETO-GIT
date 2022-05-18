

numero = int(input("Digite um número inteiro: "))
def e_primo(n):
        multiplo = 0
        m = n
        if n == 1 or n == 0 or n == -1:
            print("não primo")
        else:
            if n > 0:
                while m > 0:
                    result = n % m
                    if result == 0:
                        multiplo = multiplo + 1
                    m = m - 1
            elif n < 0:
                while m < 0:
                    result = n % m
                    if result == 0:
                        multiplo = multiplo + 1
                    m = m + 1
            if multiplo == 2:
                print("primo")
            else:
                print("não primo")


x = 1 
while x > 0:
   e_primo(n=numero)
   numero = int(input("Digite um número inteiro: "))
            




















       
