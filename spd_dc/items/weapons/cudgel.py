from .base import Weapon


class Cudgel(Weapon):
    tier = 1
    accuracy = 1.4

    @property
    def max(self) -> int:
        return 2 * self.level + 8
