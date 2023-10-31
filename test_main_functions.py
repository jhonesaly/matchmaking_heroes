import unittest
from main_functions import *
from io import StringIO

class TestMainFunctions(unittest.TestCase):

    def test_random_hero_name(self):
        name = random_name()
        self.assertTrue(name.isalpha())  # Verifica se o nome contém apenas letras
        self.assertTrue(name[0].isupper())  # Verifica se a primeira letra é maiúscula

    def test_random_hero_xp(self):
        min_number = 1
        max_number = 11000
        xp = random_number(min_number, max_number)
        self.assertTrue(min_number <= xp <= max_number)  # Verifica se o xp está dentro do intervalo especificado

    def test_random_hero_league(self):
        hero_quantity = 10
        league = random_hero_league(hero_quantity)
        self.assertEqual(len(league), hero_quantity)  # Verifica se a quantidade de heróis é correta

    def test_lvl_info(self):
        self.assertEqual(lvl_info(500), "Ferro")
        self.assertEqual(lvl_info(1500), "Bronze")
        self.assertEqual(lvl_info(2500), "Prata")
        self.assertEqual(lvl_info(5500), "Ouro")
        self.assertEqual(lvl_info(6500), "Ouro")
        self.assertEqual(lvl_info(7500), "Platina")
        self.assertEqual(lvl_info(8500), "Ascendente")
        self.assertEqual(lvl_info(9500), "Imortal")
        self.assertEqual(lvl_info(10500), "Radiante")

        
    def test_show_heroes(self):
        hero_league = [['Hero1', 5000, 10, 5], ['Hero2', 3000, 8, 7]]
        capturedOutput = StringIO()
        sys.stdout = capturedOutput  # redireciona stdout
        show_heroes(hero_league)
        sys.stdout = sys.__stdout__  # reseta redirecionamento
        expected_output = (
            "Hero\tXP\tVictory\tDefeat\tRatio\n"
            "Hero1\t5000\t10\t5\t5\n"
            "Hero2\t3000\t8\t7\t1\n"
        )
        self.assertEqual(capturedOutput.getvalue(), expected_output)



if __name__ == "__main__":
    unittest.main()