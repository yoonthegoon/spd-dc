from .base import Weapon


class Whip(Weapon):
    tier = 3
    reach = 3

    @property
    def max(self) -> int:
        return 3 * self.level + 15
