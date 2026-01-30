from .base import Weapon


class WarScythe(Weapon):
    tier = 5
    accuracy = 0.8

    @property
    def max(self) -> int:
        return 6 * self.level + 40
