import random
import functions

from character import Character

class Monster(Character):
    def __init__(self, name="Monster"):
        super().__init__(name)
        self.combat_strength = self.roll_dice()
        self.health_points = self.roll_dice()
        self.xp_amount = self.combat_strength
        print(f"{self.name} has {self.combat_strength} and {self.health_points} health.")
        print(f"Hero will receive {self.xp_amount} XP when Monster is defeated.")

    def monster_attacks(self):
        attack_power = self.combat_strength + self.roll_dice()
        print(f"{self.name} attacks with {attack_power}!")
        print(f"{self.name} has {self.health_points} health remaining.")
        return attack_power

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector.")
        super().__del__()



