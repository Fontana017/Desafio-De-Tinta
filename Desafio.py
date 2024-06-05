#   Desenvolva um programa onde calcule a area de uma 
#   parede e descubra o qunato de tinta sera gasto para pinta-lá

CORAL = 3
SUVINIL = 6
L = 1

Nome = input("Qual seu nome?")
print("Olá", Nome, "Vamos Descobrir o quanto de tinta você precisa")

Area = eval(input("Digite a altura e o comprimento da parede que você deseja pintar (separados por um *)"))

tinta = int(input("Qual a tinta? 1 - CORAL, 2 - SUVINIL: "))

if tinta == 1:
    LTS = (L * Area) / CORAL
    print("Você precisará de", LTS, "litros de tinta CORAL para pintar sua parede")

elif tinta == 2:
    LTS2 = (L * Area) / SUVINIL
    print("Você precisará de", LTS2, "litros de tinta SUVINIL para pintar sua parede")

else:
    print("Você não precisará de tinta para pintar")
