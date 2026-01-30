from .base import Weapon


class Spear(Weapon):
    tier = 2
    delay = 1.5
    reach = 2

    @property
    def max(self) -> int:
        return 4 * self.level + 20
