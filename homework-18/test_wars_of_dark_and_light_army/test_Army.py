import unittest
from Army import DarkArmy, LightArmy, Swordsman, Archer


class TestArmy(unittest.TestCase):

    def SetUpClass(cls) -> None:
        print("Test started")

    def testDownClass(cls) -> None:
        print('Test finished')

    def test_train_swordsman_return_Worrior(self):
        army = DarkArmy()
        test_swordsman = army.train_swordsman('Steve', 100)
        self.assertIsInstance(test_swordsman, Swordsman)

    def test_train_archer_return_Archer(self):
        army = DarkArmy()
        test_archer = army.train_archer('Steve', 100)
        self.assertIsInstance(test_archer, Archer)
