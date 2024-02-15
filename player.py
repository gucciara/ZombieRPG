import datetime
import random

"""
Parent class of Player and NPC. 
"""
class Character:
    def __init__(self):
        self.__health = 100
        self.__attack = random.randint(20, 30)
        self.__defense = random.randint(5, 15)
        self.__in_battle = False

    """
    Damage is the attacker's total attack minus the target's total defense. Minimum damage is 0.
    """
    def take_damage(self, enemy) -> int:
        if not isinstance(enemy, Character):
            raise TypeError("Enemy must be a Character")
        damage = enemy.attack - self.defense
        damage = int(damage)
        if damage < 0:
            return 0
        self.health -= damage
        return damage

    @property
    def health(self):
        if self.__health <= 0:
            if self.__class__.__name__ == 'NPC':
                raise NPCDeathException("NPC died.", self)
            raise PlayerDeathException('Player dies.', self)
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


class Player(Character):
    def __init__(self):
        super().__init__()
        self.__hunger = 100
        self.defense = int(self.defense * 1.5)
        self.attack = int(self.attack * 1.5)

    """
    A random amount is added to the player's hunger meter after they defeat an enemy. returns the amount
    """
    def consume(self):
        amount = random.randint(10, 30)
        self.hunger += amount
        return amount

    """
    hunger is supposed to decrease when the player is in the overworld but NOT during battle. Bool parameter should 
    be set to 'True' for when you want this function to be active.
    """
    def decrease_hunger(self) -> int:
        last_tick = datetime.datetime.now()
        while self.in_battle and self.hunger > 0:
            if datetime.datetime.now() - last_tick > datetime.timedelta(seconds=1):
                self.hunger -= 1
                last_tick = datetime.datetime.now()
        if self.hunger <= 0:
            PlayerDeathException("Player died of hunger", self)
        return self.hunger

    @property
    def hunger(self):
        return self.hunger

    @hunger.setter
    def hunger(self, hunger):
        self.__hunger = hunger


# might add more to this later
class NPC(Character):
    def __init__(self):
        super().__init__()


# These classes are for when a player or enemy dies in battle
class PlayerDeathException(Exception):
    def __init__(self, st, player):
        super().__init__(self, st)
        self.__player = player

    @property
    def character(self):
        return self.__player


class NPCDeathException(Exception):
    def __init__(self, st, npc):
        super().__init__(self, st)
        self.__NPC = npc

    @property
    def character(self):
        return self.__NPC

p = Player()
n = NPC()



