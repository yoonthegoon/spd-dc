from .base import Weapon


class RunicBlade(Weapon):
    tier = 4

    @property
    def max(self) -> int:
        return 6 * self.level + 20
