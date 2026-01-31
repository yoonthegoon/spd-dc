import tomllib
from pathlib import Path

from pydantic import BaseModel, Field, field_validator

from .aliases import ArmorAugment, TrinketKind, WeaponAugment, WeaponKind

ROOT_DIR = Path(__file__).parent.parent.absolute()


class HeroConfig(BaseModel):
    level: int = Field(default=1, ge=1, le=30)
    strength: int = Field(default=10, ge=10, le=20)


class WeaponConfig(BaseModel):
    kind: WeaponKind
    level: int = Field(default=0, ge=0)
    augment: WeaponAugment = None
    mastered: bool = False


class ArmorConfig(BaseModel):
    tier: int = Field(ge=1, le=5)
    level: int = Field(default=0, ge=0)
    augment: ArmorAugment = None
    mastered: bool = False


class EnemyConfig(BaseModel):
    accuracy: int = Field(ge=0)
    attack: tuple[int, int]
    defense: tuple[int, int]
    delay: float = Field(default=1.0, ge=0)
    evasion: int = Field(ge=0)

    @field_validator("attack", "defense", mode="before")
    @classmethod
    def validate_range(cls, value: tuple[int, int]) -> tuple[int, int]:
        a, b = value
        if not 0 <= a <= b:
            raise ValueError(f"invalid range: {a}-{b}")
        return value


class TrinketConfig(BaseModel):
    kind: TrinketKind
    level: int = Field(default=0, ge=0, le=3)


class Config(BaseModel):
    hero: HeroConfig = HeroConfig()
    weapon: WeaponConfig | None = None
    armor: ArmorConfig | None = None
    enemy: EnemyConfig | None = None
    trinket: TrinketConfig | None = None


def get_config(file: Path = ROOT_DIR / "config.toml") -> Config:
    with open(file, "rb") as f:
        return Config(**tomllib.load(f))
