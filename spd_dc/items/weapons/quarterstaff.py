from spd_dc.drv import Drv, uniform

from .base import Weapon


class Quarterstaff(Weapon):
    tier = 2

    @property
    def defense(self) -> Drv:
        return uniform(0, 2)

    @property
    def max(self) -> int:
        return 3 * self.level + 12
