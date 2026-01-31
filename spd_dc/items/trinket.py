from spd_dc.aliases import TrinketKind
from spd_dc.config import TrinketConfig


class Trinket:
    def __init__(self, kind: TrinketKind, level: int) -> None:
        self.kind = kind
        self.level = level

    @classmethod
    def from_config(cls, config: TrinketConfig | None) -> "Trinket | None":
        if config is None:
            return None
        return cls(**config.model_dump())
