from .base import Weapon


class Sai(Weapon):
    tier = 3
    delay = 0.5

    @property
    def max(self) -> int:
        return 2 * self.level + 10
