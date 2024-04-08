#Larissa Regina da Silva RA 1051392411026

'''Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e nota 2. O sistema deverá informar a ele as seguintes mensagens:a)Se a média for maior ou igual a sete: Parabéns, você está aprovado!b)Se  a média  for  menor  que  sete:  Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.'''

#Entrada dos valores do enunciado
nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))

#Cálculo da média
media = (nota1 + nota2) / 2

#Primeira condição
if media >= 7:
    print("Parabéns, você está aprovado!")

#Segunda condição
else:
    print("Você ainda tem uma chance! Estude mais para o próximo exame.")

#Inserida nota do novo exame

exame = float(input("Informe a sua nota no novo exame: "))

#Calculo entre as duas médias
mediaNova = (media + exame) / 2

#Primeira condição
if mediaNova >= 5:
    print("Parabéns, você aproveitou a sua chance! Está aprovado.")

#Segunda condição
else:
    print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")