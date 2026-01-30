from spd_dc.drv import Drv, uniform

from .base import Weapon


class Greatshield(Weapon):
    tier = 5

    @property
    def defense(self) -> Drv:
        return uniform(0, 2 * self.level + 6)

    @property
    def max(self) -> int:
        return 3 * self.level + 20
