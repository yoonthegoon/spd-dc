from spd_dc.aliases import WeaponKind
from spd_dc.config import WeaponConfig

from .base import Weapon

WEAPONS: dict[WeaponKind, type[Weapon]] = {}


def from_config(config: WeaponConfig | None) -> Weapon | None:
    if config is None:
        return None
    return WEAPONS[config.kind](
        level=config.level, augment=config.augment, mastered=config.mastered
    )
