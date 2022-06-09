nome = input("Digite um nome: ").strip()
print("O nome em maiúsculo é", nome.lower())
print("O nome em maiúsculo", nome.upper())
print("O nome possui", len(nome) - nome.count(" "), "letras")
new_name = nome.split()
print("O primeiro nome possui", len(new_name[0]), "letras")

