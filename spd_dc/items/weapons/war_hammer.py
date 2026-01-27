from .base import Weapon


class WarHammer(Weapon):
    tier = 5
    accuracy = 1.2

    @property
    def max(self) -> int:
        return 6 * self.level + 24
