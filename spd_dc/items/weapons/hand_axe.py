from .base import Weapon


class HandAxe(Weapon):
    tier = 2
    accuracy = 1.32

    @property
    def max(self) -> int:
        return 3 * self.level + 12
