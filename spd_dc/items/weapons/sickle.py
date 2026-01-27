from .base import Weapon


class Sickle(Weapon):
    tier = 2
    accuracy = 0.68

    @property
    def max(self) -> int:
        return 3 * self.level + 20
