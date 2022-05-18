x1 = float(input("Digite um número: "))
y1 = float(input("Digite um número: "))

x2 = float(input("Digite um número: "))
y2 = float(input("Digite um número: "))

dx_y = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

#import math

#math.sqrt(dx_y)

if dx_y > 10:
   print("longe")
   print(dx_y)

else:
   print("perto")
   print(dx_y)

