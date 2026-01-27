from typing import Literal

ArmorAugment = Literal["defense", "evasion"] | None

WeaponAugment = Literal["damage", "speed"] | None

WeaponKind = Literal[
    "worn shortsword",
    "mage's staff",
    "dagger",
    "studded gloves",
    "rapier",
    "cudgel",
    "shortsword",
    "hand axe",
    "spear",
    "quarterstaff",
    "dirk",
    "sickle",
    "pickaxe",
    "sword",
    "mace",
    "scimitar",
    "round shield",
    "sai",
    "whip",
    "longsword",
    "battle axe",
    "flail",
    "runic blade",
    "assasin's blade",
    "crossbox",
    "katana",
    "greatsword",
    "war hammer",
    "glaive",
    "greataxe",
    "greatshield",
    "stone gauntlet",
    "war scythe",
]
