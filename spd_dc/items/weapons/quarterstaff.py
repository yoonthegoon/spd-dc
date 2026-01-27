from spd_dc.math import Dud, Pmf

from .base import Weapon


class Quarterstaff(Weapon):
    tier = 2

    @property
    def defense(self) -> Pmf:
        return Dud(0, 2)

    @property
    def max(self) -> int:
        return 3 * self.level + 12
