import random
import functions
from character import Character


health_points_increase = 12
combat_strength_increase = 5
xp_multiplier = 1.5

class Hero (Character):
    def __init__(self, name="Hero"):
        super().__init__(name)
        self.combat_strength = self.roll_dice()
        self.health_points = self.roll_dice()
        self.level = 1
        self.xp = 1
        self.xp_level_up = 5
        print(f"{self.name} has {self.combat_strength} combat strength and {self.health_points} health.")
        print(f"{self.name} has {self.level} level.")

    def hero_attacks(self):
        attack_power = self.combat_strength + self.roll_dice()
        print(f"{self.name} attacks with {attack_power}!")
        print(f"{self.name} has {self.health_points} health remaining.")
        return attack_power

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} has gained {amount} XP!")

        if self.xp >= self.xp_level_up:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_level_up
        self.xp_level_up = int(self.xp_level_up * xp_multiplier)
        self.health_points += health_points_increase
        self.combat_strength += combat_strength_increase
        print(f"{self.name} has leveled up! {self.name} is now level {self.level}.")


    def __del__(self):
        super().__del__()
        print("The Hero object is being destroyed by the garbage collector.")


