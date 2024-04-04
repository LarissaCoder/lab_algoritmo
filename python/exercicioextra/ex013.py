#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta. pinta uma área de 2m2.

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

area = larg*alt

tinta = area/2

print("Para pintar a sua casa de área {:.2f}m², você precisará de {:.2f} litros de tinta.".format(area, tinta))