from spd_dc.drv import Drv, uniform

from .base import Weapon


class Katana(Weapon):
    tier = 4

    @property
    def defense(self) -> Drv:
        return uniform(0, 3)

    @property
    def max(self) -> int:
        return 5 * self.level + 20
