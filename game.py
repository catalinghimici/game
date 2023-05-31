from skills import CriticalStrike, Resilience, SkillType
from character import Character
import random
import json

skills = {
    "Critical strike": CriticalStrike(),
    "Resilience": Resilience()
}

class Game:
    """Game logic is defined in this class"""

    def __init__(self):
        # Read the JSON config file
        with open('config.json') as file:
            config = json.load(file)

        # Create character objects
        character1_data = config['character1']
        self.player1 = Character(
            name=character1_data['name'],
            health=random.randint(character1_data['health']['min'], character1_data['health']['max']),
            strength=random.randint(character1_data['strength']['min'], character1_data['strength']['max']),
            defense=random.randint(character1_data['defense']['min'], character1_data['defense']['max']),
            speed=random.randint(character1_data['speed']['min'], character1_data['speed']['max']),
            luck=random.uniform(character1_data['luck']['min'], character1_data['luck']['max'])
        )
        for skill in character1_data['skills']:
            self.player1.add_skill(skills[skill])

        character2_data = config['character2']
        self.player2 = Character(
            name=character2_data['name'],
            health=random.randint(character2_data['health']['min'], character2_data['health']['max']),
            strength=random.randint(character2_data['strength']['min'], character2_data['strength']['max']),
            defense=random.randint(character2_data['defense']['min'], character2_data['defense']['max']),
            speed=random.randint(character2_data['speed']['min'], character2_data['speed']['max']),
            luck=random.uniform(character2_data['luck']['min'], character2_data['luck']['max'])
        )
        for skill in character2_data['skills']:
            self.player2.add_skill(skills[skill])

        self.number_of_rounds = config['number_of_rounds']

    def play(self):
        """Gameplay defined here"""
        print(f'{self.player1}\nVERSUS\n{self.player2}')
        # Determine turn order based on speed
        if self.player1.speed > self.player2.speed:
            attacker, defender = self.player1, self.player2
        else:
            attacker, defender = self.player2, self.player1

        rounds_left = self.number_of_rounds
        # Main game loop
        while self.player1.is_alive() and self.player2.is_alive() and rounds_left:
            # Update cooldown for all skills
            for skill in attacker.skills:
                if skill.skill_type == SkillType.ATTACK:
                    skill.update_cooldown()
            for skill in defender.skills:
                if skill.skill_type == SkillType.DEFENSE:
                    skill.update_cooldown()
            # Check if defender is lucky and skip turn if true
            if defender.is_lucky():
                print(f"{defender.name} is lucky and skips the turn!")
            else:
                # Attacker attacks
                damage = attacker.attack()

                # Defender defends
                damage = defender.defend(damage)

                defender.take_damage(damage)
            
            # Swap attacker and defender for the next turn
            attacker, defender = defender, attacker
            # Decrease number of rounds left
            rounds_left = rounds_left - 1

        if not self.player1.is_alive():
            self.print_winner(self.player2)
        elif not self.player2.is_alive():
            self.print_winner(self.player1)
        elif rounds_left <= 0:
            print('It is a draw!')

    def print_winner(self, player):
        print(f'{player.name} has won!!!')

if __name__ == '__main__':
    # Create game instance
    game = Game()

    # Start the game
    game.play()
