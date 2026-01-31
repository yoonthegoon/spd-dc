from spd_dc.actors.base import Actor
from spd_dc.actors.enemy import Enemy
from spd_dc.actors.hero import Hero
from spd_dc.config import get_config

config = get_config()
hero = Hero.from_config(config)
_enemy = Enemy.from_config(config)
enemy: Actor = hero if _enemy is None else _enemy
