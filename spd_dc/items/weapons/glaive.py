from .base import Weapon


class Glaive(Weapon):
    tier = 5
    delay = 1.5
    reach = 2

    @property
    def max(self) -> int:
        return 8 * self.level + 40
