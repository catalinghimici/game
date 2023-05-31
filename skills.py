import random
from enum import Enum

class SkillType(Enum):
    ATTACK = 'Attack'
    DEFENSE = 'Defense'

class Skill:
    def __init__(self, name, chance, skill_type, cooldown):
        self.name = name
        self.chance = chance
        self.skill_type = skill_type
        self.cooldown = cooldown
        self.current_cooldown = 0

    def can_use_skill(self):
        return random.random() <= self.chance #self.current_cooldown == 0 and 

    def skill_cooldown(func):
        """Manages the cooldown period"""
        def wrapper(self, damage):
            if self.current_cooldown:
                print(f"{self.name} is on cooldown or cannot be used now.")
                return damage

            self.current_cooldown = self.cooldown
            return func(self, damage)

        return wrapper

    @skill_cooldown
    def perform_skill(self, damage):
        pass

    def update_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

class CriticalStrike(Skill):
    STRIKES = 2
    CRIT_CHANCE = 0.1
    CRIT_STRIKES = 3
    def __init__(self):
        super().__init__(name="Critical strike",
                       chance=0.1,
                       skill_type=SkillType.ATTACK,
                       cooldown=0)

    @Skill.skill_cooldown
    def perform_skill(self, damage):
        if random.random() <= self.CRIT_CHANCE:
            total_strikes = self.CRIT_STRIKES
        else:
            total_strikes = self.STRIKES

        updated_damage = damage * total_strikes
        print(f"{self.name} activated! {total_strikes} strikes dealt!")
        return updated_damage


class Resilience(Skill):
    DAMAGE_REDUCTION_FACTOR = 0.5
    def __init__(self):
        super().__init__(name="Resilience",
                       chance=0.2,
                       skill_type=SkillType.DEFENSE,
                       cooldown=2)

    @Skill.skill_cooldown
    def perform_skill(self, damage):
        reduced_damage = damage * self.DAMAGE_REDUCTION_FACTOR
        print(f"{self.name} activated! Damage reduced by {int((1 - self.DAMAGE_REDUCTION_FACTOR) * 100)}%!")
        return reduced_damage
