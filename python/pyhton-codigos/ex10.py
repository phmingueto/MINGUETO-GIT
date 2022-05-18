notas = []
while len(notas) < 6:
    nota = int(input("Qual a nota do aluno: "))
    notas.append(nota)

    
def avaliar(notas):
    for nota in notas:
        if nota <3:
            print("reprovado")
        elif nota >= 3 and nota <=5:
            print("recuperação")
        elif nota > 5 and nota <= 8:
            print("aprovado")
        elif nota > 8 and nota <= 10:
            print("muito bom")


avaliar(notas=notas)

