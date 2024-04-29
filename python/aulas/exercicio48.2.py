#Larissa Regina da Silva RA 1051392411026

def verificar_idade():
    
    # Solicita o nome e idade do usuário
    nome = input("Digite seu nome: ")  
    idade = int(input("Digite sua idade: "))  

    # Verifica se o usuário tem mais de 65 anos
    if idade > 65:
        
        print(f"Bem-vindo {nome}, você tem mais de 65 anos.")
        
     # Verifica se o usuário é maior de idade
    elif idade >= 18:
        print(f"Bem-vindo {nome}, você é maior de idade.")
        
      # Se não for maior de 18 anos, é considerado menor de idade  
    else:
        
        print(f"Bem-vindo {nome}, você é menor de idade.")

# Chama a função para iniciar o programa
verificar_idade()  