from spd_dc.config import Config
from spd_dc.drv import Drv, uniform
from spd_dc.items.trinket import Trinket

from .base import Actor


class Enemy(Actor):
    def __init__(
        self,
        accuracy: int,
        attack: tuple[int, int],
        defense: tuple[int, int],
        evasion: int,
        delay: float = 1.0,
    ) -> None:
        super().__init__()
        self._accuracy = accuracy
        self._attack = attack
        self._defense = defense
        self._evasion = evasion
        self.delay = delay
        self.trinket: Trinket | None = None

    @classmethod
    def from_config(cls, config: Config) -> "Enemy | None":
        if config.enemy is None:
            return None
        enemy = cls(**config.enemy.model_dump())
        enemy.trinket = Trinket.from_config(config.trinket)
        return enemy

    @property
    def accuracy(self) -> int:
        return self._accuracy

    @property
    def attack(self) -> Drv:
        a, b = self._attack
        return uniform(a, b)

    @property
    def defense(self) -> Drv:
        a, b = self._defense
        return uniform(a, b)

    @property
    def evasion(self) -> int:
        evasion = self._evasion
        if self.trinket is not None and self.trinket.kind == "ferret tuft":
            evasion *= 1 + 0.125 * self.trinket.level
        return int(evasion)
