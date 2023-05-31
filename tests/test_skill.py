import unittest
from unittest.mock import patch
from ..skills import SkillType, Skill, CriticalStrike, Resilience


class TestSkill(unittest.TestCase):
    def test_can_use_skill(self):
        # 100% chance and no cooldown
        skill = Skill(name="Test Skill", chance=1, skill_type=SkillType.ATTACK, cooldown=0)
        self.assertTrue(skill.can_use_skill())


    def test_cannot_use_skill_no_chance(self):
        # 0% chance and no cooldown
        skill = Skill(name="Test Skill", chance=0, skill_type=SkillType.ATTACK, cooldown=0)
        self.assertFalse(skill.can_use_skill())    


    def test_skill_cooldown_decorator(self):
        skill = Skill(name="Test Skill", chance=1, skill_type=SkillType.ATTACK, cooldown=2)
        skill.current_cooldown = 0

        @Skill.skill_cooldown
        def perform_skill(self, damage):
            return damage*2

        # test skill is performed and cooldown applied
        self.assertEqual(perform_skill(skill, 10), 20)
        self.assertEqual(skill.current_cooldown, 2)

        # test skill is in cooldown and initial value is returned
        with patch('builtins.print') as mock_print:
            self.assertEqual(perform_skill(skill, 10), 10)
            mock_print.assert_called()
    
    def test_update_cooldown(self):
        skill = Skill(name="Test Skill", chance=1, skill_type=SkillType.ATTACK, cooldown=2)
        skill.current_cooldown = 2

        skill.update_cooldown()
        self.assertEqual(skill.current_cooldown, 1)


class TestCriticalStrike(unittest.TestCase):
    def test_perform_skill(self):
        skill = CriticalStrike()

        with patch.object(skill, 'chance', 1):
            damage = skill.perform_skill(10)
            self.assertGreater(damage, 10)


class TestResilience(unittest.TestCase):
    def test_perform_skill(self):
        skill = Resilience()

        with patch.object(skill, 'chance', 1):
            damage = skill.perform_skill(10)
            self.assertLess(damage, 10)


if __name__ == "__main__":
    unittest.main()
