from spd_dc.config import EnemyConfig
from spd_dc.drv import Drv, uniform

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

    @classmethod
    def from_config(cls, config: EnemyConfig | None) -> "Enemy | None":
        if config is None:
            return None
        return cls(**config.model_dump())

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
        return self._evasion
