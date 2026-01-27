from abc import ABC, abstractmethod

from spd_dc.math import Pmf


class Actor(ABC):
    delay: float = 1.0

    @property
    @abstractmethod
    def accuracy(self) -> float: ...

    @property
    @abstractmethod
    def attack(self) -> Pmf: ...

    @property
    @abstractmethod
    def defense(self) -> Pmf: ...

    @property
    @abstractmethod
    def evasion(self) -> float: ...

    def damage_distribution(self, other: "Actor") -> Pmf:
        p = self.hit_probability(other)
        q = 1 - p
        result = self.hit_distribution(other).copy() * p
        result[0] += q
        return result

    def expected_damage(self, other: "Actor") -> float:
        return self.damage_distribution(other).mean

    def expected_damage_rate(self, other: "Actor") -> float:
        return self.expected_damage(other) / self.delay

    def hit_distribution(self, other: "Actor") -> Pmf:
        return (self.attack - other.defense).clamped(0)

    def hit_probability(self, other: "Actor") -> float:
        return (
            1 - other.evasion / (2 * self.accuracy)
            if self.accuracy > other.evasion
            else self.accuracy / (2 * other.evasion)
        )
