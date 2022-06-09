import random

a = input("Digite um aluno: ")
b = input("Digite um aluno: ")
c = input("Digite um aluno: ")
d = input("Digite um aluno: ")

lista = [a, b, c, d]

print("O aluno vencedor é:", random.choice(lista))