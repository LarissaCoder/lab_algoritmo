#Larissa Regina da Silva RA 1051392411026

#Primeiro, recebo as informações de Nome, RA, nota 1 e nota 2 pelo usuário.
nome = str(input("Digite o seu nome: "))
ra = int(input("Digite o seu RA: "))
NP1 = float(input("Digite a sua nota da primeira prova: "))
NP2 = float(input("Digite a sua nota da segunda prova: "))

#Calculo a média geral dentro de uma nova variável, com os valores do input anterior.
media = (NP1*4 + NP2*6) / 10

#Inicio a condição SE, se a média for igual ou maior do que 9, o aluno está aprovado.
if media >= 9.0:
    print(f"A sua média geral é {media:.1f}. Parabéns! Você está APROVADO.")

#Próxima condição, se a média for igual ou maior do que 7, o aluno ainda está aprovado.
elif media >= 7.0:
    print(f"A sua média geral é {media:.1f}. Parabéns! Você está APROVADO.")

#Próxima condição, se a média for igual ou maior do que 3, o aluno tem mais uma chance com o próximo exame.
elif media >= 3.0:
    print(f"A sua média geral é {media:.1f}. Ainda há uma chance, faça o próximo EXAME.")

#Última condição, se nada do que foi descrito anteriormente se encaixa (ou seja, valores menores do que 3), o aluno está reporvado.
else:
    print(f"A sua média geral é {media:.1f}. Você está de DP.")