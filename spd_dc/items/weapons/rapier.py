from spd_dc.drv import Drv, uniform

from .base import Weapon


class Rapier(Weapon):
    tier = 1

    @property
    def defense(self) -> Drv:
        return uniform(0, 1)

    @property
    def max(self) -> int:
        return 2 * self.level + 8
