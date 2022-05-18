

altura = int(input("Digite à altura do retangulo: "))
largura = int(input("Digite à largura retangulo: "))

posicao = 0

while largura > 0:
     print(end = "")
     while altura > posicao:
         print("#", end = "")
         posicao = posicao + 1
         
     posicao = 0    
     print("")   
     largura = largura - 1
         
     
