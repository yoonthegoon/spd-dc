from .base import Weapon


class Crossbow(Weapon):
    tier = 4
    accuracy = 1.24

    @property
    def max(self) -> int:
        return 4 * self.level + 20
