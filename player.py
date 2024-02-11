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
        # if self.__health <= 0:
            # if self.__class__.__name__ == 'NPC':
                # raise MonsterDeathException("NPC died.", self)
            # raise CharacterDeathException('Character dies.', self)
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
    def decrease_hunger(self, active: bool) -> int:
        last_tick = datetime.datetime.now()
        while active and self.hunger > 0:
            if datetime.datetime.now() - last_tick > datetime.timedelta(seconds=1):
                self.hunger -= 1
                last_tick = datetime.datetime.now()
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


p = Player()
n = NPC()



