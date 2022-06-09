sexo = input("Escolha um SEXO [M/F]: ").strip().upper()

while sexo not in 'MF':
        print("Opção inválida!")
        sexo = input("Escolha um SEXO [M/F]: ").strip().upper()

print("Sexo {} registrado!".format(sexo))
