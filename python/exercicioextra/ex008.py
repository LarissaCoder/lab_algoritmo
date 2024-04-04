#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número: "))

print("O dobro de {} é {}, seu triplo {} e sua raiz quadrada {:.0f}.".format(n, (n*2), (n*3), (n**1/2)))