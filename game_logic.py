"""
Monty Hall Problem - Individual Game Logic
Handles the mechanics of a single Monty Hall game.
"""

import random

class MontyHallGame:
    """Represents a single game of the Monty Hall Problem."""
    
    def __init__(self):
        self.doors = [0, 0, 0]  # 0 = goat, 1 = car
        self.car_position = None
        self.player_choice = None
        self.host_opens = None
        self.remaining_door = None
        
    def setup_game(self):
        """Set up a new game with random car placement and player choice."""
        self.doors = [0, 0, 0]
        self.car_position = random.randint(0, 2)
        self.doors[self.car_position] = 1
        self.player_choice = random.randint(0, 2)
        self.host_opens = self._get_host_choice()
        self.remaining_door = self._get_remaining_door()
    
    def _get_host_choice(self):
        """Host opens a goat door that isn't the player's choice."""
        available = [i for i in range(3) if i != self.player_choice and self.doors[i] == 0]
        return random.choice(available)
    
    def _get_remaining_door(self):
        """Find the door that is neither player's choice nor host's opened door."""
        for i in range(3):
            if i != self.player_choice and i != self.host_opens:
                return i
        return None
    
    def play_stay_strategy(self):
        self.setup_game()
        return self.doors[self.player_choice] == 1
    
    def play_switch_strategy(self):
        self.setup_game()
        return self.doors[self.remaining_door] == 1
    
    def validate_game_rules(self):
        if sum(self.doors) != 1:
            return False
        if self.host_opens is None or self.doors[self.host_opens] != 0:
            return False
        if self.host_opens == self.player_choice:
            return False
        return self.remaining_door is not None
