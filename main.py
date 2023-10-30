# Base da aplicação
import os
from main_functions import *

# Configurações iniciais

print("Bem-vindo ao ranking dos heróis!")
herois = random_hero_league(10)

while True:

    os.system('cls')

    # Listando heróis
    print("Os heróis disponíveis são:")
    for heroi in herois:
        print(heroi[0])

    # Input de herói escolhido
    heroi_escolhido = input("Por favor, escolha um herói da lista para saber o seu nível: ")

    # Verifica se escolha está na lista

    heroi_na_lista = False

    for heroi in herois:
        if heroi[0] == heroi_escolhido:
            heroi_na_lista = True
            xp_heroi = heroi[1]
            break

    if heroi_na_lista:
        # Mostrando nível do herói
        nivel_heroi = lvl_info(xp_heroi)
        print(f"O Herói de nome **{heroi_escolhido}** está no nível de **{nivel_heroi}**")

    else:
        print("Esse herói não está na lista.")
        novo_heroi = input("Deseja adicioná-lo? [s/n] ")

        if novo_heroi.lower() == 's':
            novo_xp = int(input(f"Digite o xp do herói {heroi_escolhido}: "))
            herois.append([heroi_escolhido, novo_xp])

            continue
        else:
            continue

    fim = input("Deseja parar [s]? ")

    if fim.lower() == 's':
        print("Até a próxima!")
        break

    else:
        print("Continuando...")

