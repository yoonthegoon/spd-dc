from .base import Weapon


class Dagger(Weapon):
    tier = 1

    @property
    def max(self) -> int:
        return 2 * self.level + 8
