from spd_dc.math import Dud, Pmf

from .base import Weapon


class Katana(Weapon):
    tier = 4

    @property
    def defense(self) -> Pmf:
        return Dud(0, 3)

    @property
    def max(self) -> int:
        return 5 * self.level + 20
