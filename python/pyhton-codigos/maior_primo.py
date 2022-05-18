


def maior_primo(numero_final):
    numero_avaliado = 0
    posicao = 0
    maior_primo = 0
    
    while numero_avaliado < numero_final:
        
        numero_avaliado = numero_avaliado + 1
        check_primo = True
        numero_de_divisores = 0

        while check_primo == True:
            posicao = posicao + 1
            resultado = numero_avaliado % posicao

            if resultado == 0:
                numero_de_divisores = numero_de_divisores + 1
                    
            if posicao == numero_avaliado:
                posicao = 0
                check_primo = False

                if numero_de_divisores == 2:
                    novo_primo = numero_avaliado

                    if novo_primo > maior_primo:
                        maior_primo = novo_primo
            
    return(maior_primo)


maior_primo(numero_final=10)
        
    

