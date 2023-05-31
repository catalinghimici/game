from skills import SkillType
import random

class Character:
    def __init__(self, name, health, strength, defense, speed, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.skills = []

    def add_skill(self, skill):
        """Adds an extra skill"""
        self.skills.append(skill)

    def attack(self):
        """Calculates the value of attack damage using skills/attack
        @return: float"""
        damage = self.strength
        for skill in self.skills:
            if skill.skill_type == SkillType.ATTACK and skill.can_use_skill():
                damage = skill.perform_skill(self.strength)
                break
        return damage

    def take_damage(self, damage):
        """Damage is substracted from health attribute"""
        actual_damage = max(0, damage)
        self.health -= actual_damage
        print(f"{self.name} took {actual_damage} damage. {self.health} health remaining.")

    def is_alive(self):
        """Checks if the character still has health points"""
        return self.health > 0

    def defend(self, incomming_damage: float) -> float:
        """Reduces the incomming damage appling available skills/defence
        @param incomming_damage: float
        @return: float remaining damage after defence was applied"""
        damage_taken = incomming_damage - self.defense
        for skill in self.skills:
            if skill.skill_type == SkillType.DEFENSE and skill.can_use_skill():
                damage_taken = skill.perform_skill(damage_taken)
                break
        return damage_taken

    def is_lucky(self):
        """Checks if the character is lucky for this turn"""
        return random.random() <= self.luck
    
    def __str__(self):
        return (
            f"Character: {self.name}\n\tHealth: {self.health}\n\tStrength: {self.strength}\n\tDefence: {self.defense}\n\tSpeed: {self.speed}\n\tLuck: {self.luck}\n\t"
            f"Skills: {[x.name for x in self.skills]}"
        )
