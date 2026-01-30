from spd_dc.drv import Drv, uniform

from .base import Weapon


class RoundShield(Weapon):
    tier = 3

    @property
    def defense(self) -> Drv:
        return uniform(0, self.level + 4)

    @property
    def max(self) -> int:
        return 2 * self.level + 12
