from abc import ABC, abstractmethod
from math import sqrt

from spd_dc.aliases import ArmorAugment, WeaponAugment
from spd_dc.math import Dud, Pmf


class Item[T: ArmorAugment | WeaponAugment](ABC):
    def __init__(
        self,
        tier: int,
        level: int = 0,
        augment: T = None,  # ty: ignore[invalid-parameter-default]
        mastered: bool = False,
    ) -> None:
        self.tier = tier
        self.level = level
        self.augment = augment
        self.mastered = mastered

    @property
    def strength(self) -> int:
        strength = (2 * self.tier + 8) - int((sqrt(8 * self.level + 1) - 1) / 2)
        if self.mastered:
            strength -= 2
        return strength
