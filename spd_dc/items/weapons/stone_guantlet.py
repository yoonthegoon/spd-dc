from .base import Weapon


class StoneGauntlet(Weapon):
    tier = 5
    delay = 0.5

    @property
    def max(self) -> int:
        return 3 * self.level + 15
