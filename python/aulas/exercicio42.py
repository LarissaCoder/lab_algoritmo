#Larissa Regina da Silva RA 1051392411026

'''Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e
nota 2. O sistema deverá informar a ele as seguintes mensagens:
a) Se a média for maior ou igual a sete: Parabéns, você está aprovado!
b) Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o
exame.'''

'''
#Resolvido sem função
nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print ("Parabéns, você está aprovado!")

else:
    print("Você ainda tem uma chance! Estude mais para o exame") '''
    
#Resolvido com função

import statistics

nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
p1 = float(input("Informe a sua primeira nota: "))
p2 = float(input("Informe a sua segunda nota: "))

def func_media (p1, p2):
    if statistics.mean ([p1,p2]) >=7:
        return media
    
media = func_media (p1, p2)

if media 
print("Parabéns, você está aprovado!")

else:
print("Você ainda tem uma chance! Estude mais para o exame")


