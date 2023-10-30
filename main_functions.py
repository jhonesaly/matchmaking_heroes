# Funções da aplicação

import random


def random_hero_name():
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


def random_hero_xp(min_number, max_number):
    return random.randint(min_number, max_number)


def random_hero_league(hero_quantity):
    hero_league = []
    for i in range(hero_quantity):
        hero_name = random_hero_name()
        hero_xp = random_hero_xp(1,11000)
        hero_league.append([hero_name, hero_xp])

    return hero_league


def lvl_info(hero_xp):
    if hero_xp < 1000:
        return "Ferro"
    elif 1001 <= hero_xp <= 2000:
        return "Bronze"
    elif 2001 <= hero_xp <= 5000:
        return "Prata"
    elif 5001 <= hero_xp <= 6000:
        return "Ouro"
    elif 6001 <= hero_xp <= 7000:
        return "Ouro"
    elif 7001 <= hero_xp <= 8000:
        return "Platina"
    elif 8001 <= hero_xp <= 9000:
        return "Ascendente"
    elif 9001 <= hero_xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"