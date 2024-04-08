'''#Larissa Regina da Silva RA 1051392411026 

# Solicitei valor da altura
altura = float(input("Digite sua altura (em metros): "))

# Seleção da fórmula de acordo com o sexo
sexo = input("Digite seu sexo (M/F): ")
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

# Exibi o resultado
print(f"Seu peso ideal é de aproximadamente {peso_ideal:.2f} kg.")'''

''' Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso (p) ideal, 
utilizando as seguintes fórmulas: Para homens: 
(72.7*h) -58 Para mulheres: (62.1*h) -44.7'''

h = float(input("Insira a sua altura (metros): "))
sexo = input("Qual o seu sexo? (M/F)? ")

if sexo == "M" or sexo == "m":
    peso = (72.7*h) - 58

if sexo == "F" or sexo == "f":
    peso = (62.1*h) -44.7

print(f"O seu peso ideal é de {peso:.1f}")