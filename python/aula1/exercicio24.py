#Larissa Regina da Silva RA 1051392411026 

# Solicitei valor da altura
altura = float(input("Digite sua altura (em metros): "))

# Seleção da fórmula de acordo com o sexo
sexo = input("Digite seu sexo (M/F): ")
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

# Exibi o resultado
print(f"Seu peso ideal é de aproximadamente {peso_ideal:.2f} kg.")
