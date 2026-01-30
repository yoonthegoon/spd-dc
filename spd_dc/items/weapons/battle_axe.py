from .base import Weapon


class BattleAxe(Weapon):
    tier = 4
    accuracy = 1.24

    @property
    def max(self) -> int:
        return 5 * self.level + 20
