from .base import Weapon


class Scimitar(Weapon):
    tier = 3
    delay = 0.8

    @property
    def max(self) -> int:
        return 4 * self.level + 16
