from math import sqrt

from spd_dc.aliases import ArmorAugment
from spd_dc.config import ArmorConfig
from spd_dc.math import Dud, Pmf

from .base import Item


class Armor(Item[ArmorAugment]):
    def __init__(self, tier: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tier = tier

    @classmethod
    def from_config(cls, config: ArmorConfig | None) -> "Armor | None":
        if config is None:
            return None
        return cls(**config.model_dump())

    @property
    def defense(self) -> Pmf:
        return Dud(self.min, self.max)

    @property
    def evasion(self) -> int:
        match self.augment:
            case "defense":
                return -2 * (self.level + 2)
            case "evasion":
                return 2 * (self.level + 2)
            case _:
                return 0

    @property
    def max(self) -> int:
        damage = self.tier * (self.level + 2)
        match self.augment:
            case "defense":
                damage += self.level + 2
            case "evasion":
                damage -= self.level + 2
        if self.level > damage:
            return int(((self.level - damage) + 1) / 2)
        return damage

    @property
    def min(self) -> int:
        damage = self.max
        if self.level >= damage:
            return self.level - damage
        return self.level

    @property
    def strength(self) -> int:
        strength = (2 * self.tier + 8) - int((sqrt(8 * self.level + 1) - 1) / 2)
        if self.mastered:
            strength -= 2
        return strength
