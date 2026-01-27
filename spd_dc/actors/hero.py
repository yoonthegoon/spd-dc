from spd_dc.config import Config
from spd_dc.items import weapons
from spd_dc.items.armor import Armor
from spd_dc.items.weapons import from_config
from spd_dc.items.weapons.base import Weapon
from spd_dc.math import Dud, Pmf

from .base import Actor


class Hero(Actor):
    def __init__(
        self,
        level: int = 1,
        strength: int = 10,
        weapon: Weapon | None = None,
        armor: Armor | None = None,
    ) -> None:
        self.level = level
        self._strength = strength
        self.weapon = weapon
        self.armor = armor

    @classmethod
    def from_config(cls, config: Config) -> "Hero":
        weapon = weapons.from_config(config.weapon)
        armor = Armor.from_config(config.armor)
        return cls(
            level=config.hero.level,
            strength=config.hero.strength,
            weapon=weapon,
            armor=armor,
        )

    @property
    def accuracy(self) -> int:
        accuracy = self.level + 9
        # TODO: ring of accuracy
        if self.weapon is not None:
            accuracy *= self.weapon.accuracy
        return max(1, round(accuracy))

    @property
    def attack(self) -> Pmf:
        attack = Pmf({1: 1})
        # TODO:
        # unarmed
        # ring of might
        if self.weapon is not None:
            attack = self.weapon.attack
            if self.strength > self.weapon.strength:
                attack += Dud(0, self.strength - self.weapon.strength)
        return attack

    @property
    def delay(self) -> float:
        delay = 1.0
        # TODO: ring of furor
        if self.weapon is not None:
            delay *= self.weapon.augmented_delay
            if self.strength < self.weapon.strength:
                delay *= 1.2 ** (self.weapon.strength - self.strength)
        return delay

    @property
    def defense(self) -> Pmf:
        # TODO: check if this is right
        defense = Pmf({0: 1})
        if self.armor is not None:
            defense = self.armor.defense
        if self.weapon is not None:
            defense += self.weapon.defense
        return defense

    @property
    def evasion(self) -> int:
        evasion = self.level + 4
        # TODO:
        # ring of evasion
        # ferret tuft
        if self.armor is not None:
            # TODO: check order of following 3 lines
            if self.strength < self.armor.strength:
                evasion /= 1.5 ** (self.armor.strength - self.strength)
            evasion += self.armor.evasion
        return max(1, round(evasion))

    @property
    def strength(self) -> int:
        strength = self._strength
        # TODO: ring of strength
        return strength
