#Larissa Regina da Silva RA 1051392411026

import math

#Determinei a função para calcular a media das duas notas.
def funcao_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

#Criei o input para o usuário inserir as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

resultado = funcao_media(nota1, nota2)

#Determinei as condições com base nos critérios,dependendo da media será retornado o resultado da função
if resultado >= 7 and resultado <= 10:
    print("Parabéns, você está aprovado!")
    
elif resultado < 7:
    print("Você ainda tem uma chance! Estude mais para o exame.")
    
else:
    print("O número informado é inválido.") 
    

#Determinei a função para calcular a media das duas notas junto com o novo exame.
def funcao_exame(resultado, nota_exame):
    nova_media = (resultado + nota_exame) / 2
    return nova_media

#Criei o input para o usuário inserir a nova nota
nota_exame = float(input("Digite a nota do exame: "))

novo_resultado = funcao_exame(resultado, nota_exame)

#Determinei as condições com base nos critérios,dependendo da nova media será retornado o resultado da função
if novo_resultado >= 5 and novo_resultado <= 10:
    print("Parabéns, você aproveitou a sua chance! Está aprovado.")

elif novo_resultado < 5:
    print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")

else:
    print("O número informado é inválido.") 