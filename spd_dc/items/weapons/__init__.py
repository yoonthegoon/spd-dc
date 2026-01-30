from spd_dc.aliases import WeaponKind
from spd_dc.config import WeaponConfig

from .assassins_blade import AssassinsBlade
from .base import Weapon
from .battle_axe import BattleAxe
from .crossbow import Crossbow
from .cudgel import Cudgel
from .dagger import Dagger
from .dirk import Dirk
from .flail import Flail
from .glaive import Glaive
from .greataxe import Greataxe
from .greatshield import Greatshield
from .greatsword import Greatsword
from .hand_axe import HandAxe
from .katana import Katana
from .longsword import Longsword
from .mace import Mace
from .mages_staff import MagesStaff
from .quarterstaff import Quarterstaff
from .rapier import Rapier
from .round_shield import RoundShield
from .runic_blade import RunicBlade
from .sai import Sai
from .scimitar import Scimitar
from .shortsword import Shortsword
from .sickle import Sickle
from .spear import Spear
from .stone_gauntlet import StoneGauntlet
from .studded_gloves import StuddedGloves
from .sword import Sword
from .war_hammer import WarHammer
from .war_scythe import WarScythe
from .whip import Whip
from .worn_shortsword import WornShortsword

WEAPONS: dict[WeaponKind, type[Weapon]] = {
    "worn shortsword": WornShortsword,
    "mage's staff": MagesStaff,
    "dagger": Dagger,
    "studded gloves": StuddedGloves,
    "rapier": Rapier,
    "cudgel": Cudgel,
    "shortsword": Shortsword,
    "hand axe": HandAxe,
    "spear": Spear,
    "quarterstaff": Quarterstaff,
    "dirk": Dirk,
    "sickle": Sickle,
    # "pickaxe": Pickaxe,
    "sword": Sword,
    "mace": Mace,
    "scimitar": Scimitar,
    "round shield": RoundShield,
    "sai": Sai,
    "whip": Whip,
    "longsword": Longsword,
    "battle axe": BattleAxe,
    "flail": Flail,
    "runic blade": RunicBlade,
    "assassin's blade": AssassinsBlade,
    "crossbow": Crossbow,
    "katana": Katana,
    "greatsword": Greatsword,
    "war hammer": WarHammer,
    "glaive": Glaive,
    "greataxe": Greataxe,
    "greatshield": Greatshield,
    "stone gauntlet": StoneGauntlet,
    "war scythe": WarScythe,
}


def from_config(config: WeaponConfig | None) -> Weapon | None:
    if config is None:
        return None
    return WEAPONS[config.kind](
        level=config.level, augment=config.augment, mastered=config.mastered
    )
