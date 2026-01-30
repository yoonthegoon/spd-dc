from .base import Weapon


class StuddedGloves(Weapon):
    tier = 1
    delay = 0.5

    @property
    def max(self) -> int:
        return self.level + 5
