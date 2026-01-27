from spd_dc.math import Dud, Pmf

from .base import Weapon


class Rapier(Weapon):
    tier = 1

    @property
    def defense(self) -> Pmf:
        return Dud(0, 1)

    @property
    def max(self) -> int:
        return 2 * self.level + 8
