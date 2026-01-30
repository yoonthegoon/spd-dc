from abc import ABC, abstractmethod

from spd_dc.aliases import WeaponAugment
from spd_dc.drv import Drv, constant, uniform
from spd_dc.items.base import Item


class Weapon(Item[WeaponAugment], ABC):
    accuracy: float = 1.0
    delay: float = 1.0
    reach: int = 1

    @property
    @abstractmethod
    def tier(self) -> int: ...

    @property
    def attack(self) -> Drv:
        return uniform(self.augmented_min, self.augmented_max)

    @property
    def augmented_delay(self) -> float:
        delay = self.delay
        match self.augment:
            case "damage":
                delay *= 5 / 3
            case "speed":
                delay *= 2 / 3
        return delay

    @property
    def augmented_max(self) -> int:
        damage = self.max
        match self.augment:
            case "damage":
                damage *= 1.5
            case "speed":
                damage *= 0.7
        return round(damage)

    @property
    def augmented_min(self) -> int:
        damage = self.min
        match self.augment:
            case "damage":
                damage *= 1.5
            case "speed":
                damage *= 0.7
        return round(damage)

    @property
    def defense(self) -> Drv:
        return constant(0)

    @property
    def max(self) -> int:
        return (self.level + 5) * (self.tier + 1)

    @property
    def min(self) -> int:
        return self.tier + self.level
