"""
Monty Hall Problem - Simulation Engine
Runs multiple games and collects statistics.
"""

from game_logic import MontyHallGame

class MontyHallSimulation:
    """Manages multiple Monty Hall games and collects statistics."""
    
    def __init__(self):
        self.game = MontyHallGame()
    
    def run_strategy_simulation(self, strategy, num_games):
        """Run simulation for a specific strategy ('stay' or 'switch')."""
        if strategy not in ("stay", "switch"):
            raise ValueError("Strategy must be 'stay' or 'switch'")
        
        wins = 0
        total_games = int(num_games)
        progress_interval = max(1, total_games // 10)  # 10% increments
        
        print(f"  0% complete...", end="", flush=True)
        for i in range(total_games):
            won = (self.game.play_stay_strategy() if strategy == "stay"
                   else self.game.play_switch_strategy())
            if won:
                wins += 1
            if (i + 1) % progress_interval == 0:
                pct = ((i + 1) / total_games) * 100
                print(f"\r  {pct:.0f}% complete...", end="", flush=True)
        print("\r  100% complete!")
        
        win_rate = (wins / total_games) * 100 if total_games else 0.0
        return {"strategy": strategy, "wins": wins, "total_games": total_games, "win_rate": win_rate}
    
    def run_full_simulation(self, num_games_per_strategy):
        """Run both strategies with the given per-strategy game count."""
        stay_results = self.run_strategy_simulation("stay", num_games_per_strategy)
        print()
        switch_results = self.run_strategy_simulation("switch", num_games_per_strategy)
        return stay_results, switch_results
