from abc import ABC
from random import choice
from random import randint
from time import sleep


class Army(ABC):
    def __init__(self):
        self.warriors = []

    def train_swordsman(self, name, health):
        swordsman = Swordsman(name, health, self)
        self.warriors.append(swordsman)
        return swordsman

    def train_archer(self, name, health):
        archer = Archer(name, health, self)
        self.warriors.append(archer)
        return archer


class Warrior(ABC):
    def __init__(self, name: str, health: int, army):
        self.name = name
        self._health = health
        self.army = army
        self._is_alive = True
        self.damage = 0

    def __repr__(self):
        return f"{self.name} | {self.health} | {self.army} " \
                f"| alive: {self.is_alive}"

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            print(f"{self.name} died")
            self.is_alive = False

    def hit(self, warrior):
        if isinstance(self, Swordsman) and isinstance(warrior, Archer):
            warrior.health -= self.damage * 1.5
        else:
            warrior.health -= self.damage

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value
        if self._is_alive is False:
            self.army.warriors.remove(self)


class Swordsman(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 15

class Archer(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 10


class DarkArmy(Army):
    def __repr__(self):
        return "Dark Army"


class LightArmy(Army):
    def __repr__(self):
        return "Light Army"


da = DarkArmy()
la = LightArmy()

names = ['Cerberus', 'Mordred', 'Dagda', 'Arthur', 'Aterui', 'Fenrir',
         'Sekitoba', 'Polaris', 'Susanoo', 'Nero', 'Alcatraz', 'Genezis']

for i in range(10):
    da.train_swordsman(choice(names), randint(1, 101))
    la.train_swordsman(choice(names), randint(1, 101))
    da.train_archer(choice(names), randint(1, 101))
    la.train_archer(choice(names), randint(1, 101))



if __name__ == "__main__":
    print(la.warriors)
    print(da.warriors)

    while da.warriors and la.warriors:
        sleep(0.5)
        war1 = choice(da.warriors)
        war2 = choice(la.warriors)

        print(f"{war1} hits {war2}")
        war1.hit(war2)
        print(f"{war2} hits {war1}")
        war2.hit(war1)

        print(f"_STATUS \t \t Dark Army: {len(da.warriors)} |" \
               f" Light Army: {len(la.warriors)}")

    if len(la.warriors) > 1:
        print(la.warriors)
        print('LIGHT WON!')
    else:
        print(da.warriors)
        print('DARK WON!')
