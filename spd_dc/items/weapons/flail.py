from .base import Weapon


class Flail(Weapon):
    tier = 4
    accuracy = 0.8

    @property
    def max(self) -> int:
        return 8 * self.level + 35
