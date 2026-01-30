from .base import Weapon


class MagesStaff(Weapon):
    tier = 1

    @property
    def max(self) -> int:
        return 2 * self.level + 6
