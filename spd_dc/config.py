import tomllib
from pathlib import Path

from pydantic import BaseModel, Field

from .aliases import ArmorAugment, WeaponAugment, WeaponKind

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
    mastered = False


class Config(BaseModel):
    hero: HeroConfig = HeroConfig()
    weapon: WeaponConfig | None = None
    armor: ArmorConfig | None = None


def get_config(file: Path = ROOT_DIR / "config.toml") -> Config:
    with open(file, "rb") as f:
        return Config(**tomllib.load(f))
