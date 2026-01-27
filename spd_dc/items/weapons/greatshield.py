from spd_dc.math import Dud, Pmf

from .base import Weapon


class Greatshield(Weapon):
    tier = 5

    @property
    def defense(self) -> Pmf:
        return Dud(0, 2 * self.level + 6)

    @property
    def max(self) -> int:
        return 3 * self.level + 20
