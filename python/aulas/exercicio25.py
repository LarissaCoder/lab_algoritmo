import math

#a-b) Latas de 18 litros e 3,6 litros
area = float(input("Digite a área: "))

coberturaLataG = 18 * 6
coberturaLataP = 3.6 * 6

totalLataG = area / coberturaLataG
totalLataP = area / coberturaLataP

print(f"{math.ceil(totalLataG)}")    
print(f"{math.ceil(totalLataP)}")

#c) latas e galões, o menor preço

totalComSobra = totalLataG + (totalLataG*10) / 100
print(f"{totalComSobra}")

