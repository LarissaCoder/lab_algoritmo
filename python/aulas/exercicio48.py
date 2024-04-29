#Larissa Regina da Silva RA 1051392411026

def funcao_salario():
    # Solicita ao usuário que digite o seu salário
    salario = float(input("Digite o seu salário: "))
    
    # Verifica se o salário é menor ou igual a R$1500,00
    if salario <= 1500:
        # Calcula o aumento de 20%
        aumento = (salario * 20) / 100
        
    # Verifica se o salário é maior que R$1500,00 e menor que R$2500,00
    elif salario > 1500 and salario < 2500:
        # Calcula o aumento de 10%
        aumento = (salario * 10) / 100
        
    # Para os demais valores de salário
    else:
        # Calcula o aumento de 5%
        aumento = (salario * 5) / 100
        
    # Calcula o novo salário com o aumento
    novo_salario = salario + aumento
        
    # Exibe o salário original e o novo salário com o aumento aplicado
    print(f"O seu salário era R${salario:.2f}.")
    print(f"Com o aumento o seu salário passa a ser R${novo_salario:.2f}.")

# Chama a função para iniciar o programa
funcao_salario()
