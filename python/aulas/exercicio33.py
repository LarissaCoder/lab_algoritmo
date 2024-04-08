#Larissa Regina da Silva RA 1051392411026

'''Altere o algoritmo anterior (Fix32)para que o usuário entre com a nota do exame. Lembre-se que deve se realizar a média aritmética entre a média e a nota do exame. O sistema deverá informar a ele as seguintes mensagens:a)Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado.b)Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário.'''

nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Parabéns, você está aprovado!")

else:
    print("Você ainda tem uma chance! Estude mais para o próximo exame.")
    
#segunda parte

exame = float(input("Informe a sua nota no novo exame: "))


mediaNova = (media + exame) / 2

if mediaNova >= 5:
    print("Parabéns, você aproveitou a sua chance! Está aprovado.")

else:
    print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")