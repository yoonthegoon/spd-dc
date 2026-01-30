from abc import ABC, abstractmethod

from scipy.stats import rv_discrete

from spd_dc.drv import add_probabilities, clamp, sub


class Actor(ABC):
    delay: float = 1.0

    @property
    @abstractmethod
    def accuracy(self) -> int: ...

    @property
    @abstractmethod
    def attack(self) -> rv_discrete: ...

    @property
    @abstractmethod
    def defense(self) -> rv_discrete: ...

    @property
    @abstractmethod
    def evasion(self) -> int: ...

    def damage_rv(self, other: "Actor") -> rv_discrete:
        q = 1 - self.hit_probability(other)
        hit_rv = self.hit_rv(other)
        return add_probabilities(hit_rv, [0], [q])

    def expected_damage(self, other: "Actor") -> float:
        damage_rv = self.damage_rv(other)
        return damage_rv.mean()

    def expected_damage_rate(self, other: "Actor") -> float:
        damage_rv = self.damage_rv(other)
        return damage_rv.mean() / self.delay

    def expected_hit(self, other: "Actor") -> float:
        hit_rv = self.hit_rv(other)
        return hit_rv.mean()

    def hit_rv(self, other: "Actor") -> rv_discrete:
        return clamp(sub(self.attack, other.defense), 0)

    def hit_probability(self, other: "Actor") -> float:
        return (
            1 - other.evasion / (2 * self.accuracy)
            if self.accuracy > other.evasion
            else self.accuracy / (2 * other.evasion)
        )
