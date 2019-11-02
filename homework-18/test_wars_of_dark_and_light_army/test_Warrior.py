import unittest
from Army import DarkArmy, LightArmy, Swordsman, Archer, Warrior


class TestWarrior(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("Test started")
        cls.army = DarkArmy()

    def setUp(self):
        self.swordsman = self.army.train_swordsman('Steve', 100)
        self.archer = self.army.train_archer('Steve', 100)

    def tearDown(self):
        if self.swordsman in self.army.warriors:
            self.army.warriors.remove(self.swordsman)
        if self.archer in self.army.warriors:
            self.army.warriors.remove(self.archer)

    def test_warrior_dies_when_heals_less_than_zero(self):
        self.assertTrue(self.swordsman.is_alive)
        self.swordsman.health = -3
        self.assertFalse(self.swordsman.is_alive)

    def test_warrior_is_removed_from_army_after_death(self):
        self.assertIn(self.swordsman, self.army.warriors)
        self.swordsman.health = 0
        self.assertNotIn(self.swordsman, self.army.warriors)

    def test_archer_heals_changes_correctly_when_aswordsman_hit_him(self):
        self.swordsman.hit(self.archer)
        self.assertEqual(self.archer.health, 77.5)

    def test_swordsman_heals_changes_correctly_when_archer_hit_him(self):
        self.archer.hit(self.swordsman)
        self.assertEqual(self.swordsman.health, 90)

    def test_heals_changes_correctly_when_archer_hit_archer(self):
        a1 = self.archer
        a2 = self.archer
        a1.hit(a2)
        self.assertEqual(a2.health, 90)

    def test_heals_changes_correctly_when_swordsman_hit_swordsman(self):
        s1 = self.swordsman
        s2 = self.swordsman
        s1.hit(s2)
        self.assertEqual(s2.health, 85)
