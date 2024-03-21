import asyncio
import datetime
import random

"""
Damage is the attacker's total attack minus the target's total defense. Minimum damage is 0.
"""

class Character:
    def __init__(self):
        self.__hunger = 100
        self.__health = 100
        self.__attack = random.randint(20, 30)
        self.__defense = random.randint(5, 15)
        self.__in_battle = False

    """
    A random amount is added to the player's hunger meter after they defeat an enemy. returns the amount
    """
    def consume(self):
        amount = random.randint(10, 30)
        self.hunger += amount
        return amount

    """
    hunger is supposed to decrease when the player is in the overworld but NOT during battle.
    """
    async def decrease_hunger(self) -> int:
        last_tick = datetime.datetime.now()
        while not self.in_battle and self.__hunger > 0:
            await asyncio.sleep(0.25)
            if datetime.datetime.now() - last_tick > datetime.timedelta(seconds=0.25):
                print(self.hunger)
                self.hunger -= 1
                last_tick = datetime.datetime.now()
        if self.hunger <= 0:
            raise Exception("Player died of hunger", self)
        return self.hunger

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, hunger):
        self.__hunger = hunger

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @property
    def in_battle(self):
        return self.__in_battle

    @in_battle.setter
    def in_battle(self, in_battle):
        if not isinstance(in_battle, bool):
            raise ValueError("in_battle must be a bool variable")
        self.__in_battle = in_battle




