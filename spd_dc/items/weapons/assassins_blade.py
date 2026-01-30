from .base import Weapon


class AssassinsBlade(Weapon):
    tier = 4

    @property
    def max(self) -> int:
        return 5 * self.level + 20
