from spd_dc.math import Dud, Pmf

from .base import Weapon


class RoundShield(Weapon):
    tier = 3

    @property
    def defense(self) -> Pmf:
        return Dud(0, self.level + 4)

    @property
    def max(self) -> int:
        return 2 * self.level + 12
