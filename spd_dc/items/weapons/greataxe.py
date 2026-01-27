from math import sqrt

from .base import Weapon


class Greataxe(Weapon):
    tier = 5

    @property
    def max(self) -> int:
        return 6 * self.level + 45

    @property
    def strength(self) -> int:
        strength = (2 * (self.tier + 1) + 8) - int((sqrt(8 * self.level + 1) - 1) / 2)
        if self.mastered:
            strength -= 2
        return strength
