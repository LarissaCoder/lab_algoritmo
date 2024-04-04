#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite a medida em metros: "))

cent = medida*100
mili = medida*1000

print("A medida de {} em metros, é igual a {:.0f} centímetros e {:.0f} milímetros.".format(medida,cent, mili))