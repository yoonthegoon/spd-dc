from .base import Weapon


class Dirk(Weapon):
    tier = 2

    @property
    def max(self) -> int:
        return 3 * self.level + 12
