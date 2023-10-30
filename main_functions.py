# Funções da aplicação

import random


def random_name():
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vogais = ['a', 'e', 'i', 'o', 'u']

    num_silabas = random.choice([2, 3])

    nome = ''
    
    for _ in range(num_silabas):
        consoante_aleatoria = random.choice(consoantes)
        vogal_aleatoria = random.choice(vogais)
        silaba = consoante_aleatoria + vogal_aleatoria
        nome += silaba
    
    return nome.capitalize()


def random_number(min_number, max_number):
    return random.randint(min_number, max_number)


def hero_match(hero_1, hero_2):
    hero_total_xp = hero_1[1] + hero_2[1]
    match_number = random_number(1,hero_total_xp)

    if match_number < hero_1[1]:
        hero_1[2] += 1
        hero_2[2] -= 1
        return hero_1[0]
    else:
        hero_2[2] += 1
        hero_1[2] -= 1
        return hero_2[0]


def random_hero_league(hero_quantity):
    hero_league = []
    for i in range(hero_quantity):
        hero_name = random_name()
        hero_xp = random_number(1,11000)
        hero_rating = 0
        hero_league.append([hero_name, hero_xp, hero_rating])

    return hero_league


def hero_championship(hero_league, seasons=1):
    for i in range(len(hero_league)):
        for j in range(len(hero_league))
            if i == j :
                continue
            else:
                hero_match(hero_league[i], hero_league[j])


def show_heroes(hero_league):
    for hero in hero_league:
        print("Hero/XP/Ratio")
        print(f"{hero[0]},{hero[1]},{hero[2]}")

def lvl_info(hero_xp):
    if hero_xp < 1000:
        return "Ferro"
    elif 1001 <= hero_xp <= 2000:
        return "Bronze"
    elif 2001 <= hero_xp <= 5000:
        return "Prata"
    elif 5001 <= hero_xp <= 7000:
        return "Ouro"
    elif 7001 <= hero_xp <= 8000:
        return "Platina"
    elif 8001 <= hero_xp <= 9000:
        return "Ascendente"
    elif 9001 <= hero_xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"


def rating_info(hero_rating):
    if hero_rating < 10:
        return "Ferro"
    elif 11 <= hero_rating <= 20:
        return "Bronze"
    elif 21 <= hero_rating <= 50:
        return "Prata"
    elif 51 <= hero_rating <= 80:
        return "Ouro"
    elif 81 <= hero_rating <= 90:
        return "Diamante"
    elif 91 <= hero_rating <= 100:
        return "Lendário"
    else:
        return "Imortal"

if __name__ == '__main__':

    import os
    os.system('cls')
    
    hero_league = random_hero_league(20)
    show_heroes(hero_league)
    
    print(hero_league[0])
    print('X')
    print(hero_league[1])
    winner = hero_match(hero_league[0],hero_league[1])
    print(f"o vencedor é {winner}")