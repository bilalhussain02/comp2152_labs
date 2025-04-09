import random

class Character:
    def __init__(self, name="Character"):
        self.name = name
        self._combat_strength = self.roll_dice() * 10
        self._health_points = self.roll_dice() * 10

    def roll_dice(self):
        dice = random.randint(1, 7)
        return dice

    def __del__(self):
        print(f"Character {Character} is in trouble!")

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._health_points = value


