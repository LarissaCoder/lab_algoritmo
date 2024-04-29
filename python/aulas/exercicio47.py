#Larissa Regina da Silva RA 1051392411026

def divisivel():
    numero = int(input("Digite um número: "))
    
    # Verifica se o número é divisível por 10
    if numero % 10 == 0:
        print(f"O número {numero} é divisível por 10.")
        
    # Verifica se o número é divisível por 5
    elif numero % 5 == 0:
        print(f"O número {numero} é divisível por 5.")
        
    # Verifica se o número é divisível por 2
    elif numero % 2 == 0:
        print(f"O número {numero} é divisível por 2.")
        
    # Se o número não for divisível por nenhum dos valores acima
    else:
        print(f"O número {numero} não é divisível por 10, 5 ou 2.")

# Chama a função para iniciar o programa
divisivel()
