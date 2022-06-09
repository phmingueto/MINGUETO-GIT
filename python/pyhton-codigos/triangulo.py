s1 = int(input("Digite o primeiro seguimento: "))
s2 = int(input("Digite o segundo seguimento: "))
s3 = int(input("Digite o terceiro seguimento: "))


if s3 < s1 + s2 and s1 < s2 + s3 and s3 < s2 + s1:
    print("FORMA TRIANGULO!")
    if  s1 == s2 == s3:
       print("O seguimentos descrtios formam um triangulo EQUILÁTERO")
    elif s1 != s2 != s3:
        print("O seguimentos descrtios formam um triangulo ESCALENO")
    elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print("O seguimentos descrtios formam um triangulo ISÓSCELE")

else:
    print("NÃO FORMA TRIANGULO")

