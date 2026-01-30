from .base import Weapon


class Mace(Weapon):
    tier = 3
    accuracy = 1.28

    @property
    def max(self) -> int:
        return 4 * self.level + 16
