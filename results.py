"""
Monty Hall Problem - Results Display
Formats and displays simulation results clearly.
"""

class ResultsDisplay:
    def __init__(self):
        self.theoretical = {"stay": 33.333333, "switch": 66.666667}
    
    def show_results(self, stay_results, switch_results, execution_time=None):
        print("\n" + "="*60)
        print("MONTY HALL SIMULATION RESULTS")
        print("="*60)
        self._show_strategy_results(stay_results, "STAY STRATEGY")
        print()
        self._show_strategy_results(switch_results, "SWITCH STRATEGY")
        print("\n" + "-"*60)
        print("COMPARISON")
        print("-"*60)
        self._show_comparison(stay_results, switch_results)
        print("\n" + "-"*60)
        print("THEORETICAL vs ACTUAL")
        print("-"*60)
        self._show_theoretical_comparison(stay_results, switch_results)
        print("\n" + "-"*60)
        print("CONCLUSION")
        print("-"*60)
        self._show_conclusion(stay_results, switch_results)
        if execution_time is not None:
            print("\n" + "-"*60)
            print("EXECUTION STATISTICS")
            print("-"*60)
            self._show_execution_stats(stay_results, switch_results, execution_time)
        print("\n" + "="*60)
    
    def _show_strategy_results(self, results, strategy_name):
        print(f"{strategy_name}:")
        print(f"  Total Games:    {results['total_games']:,}")
        print(f"  Wins:           {results['wins']:,}")
        print(f"  Losses:         {results['total_games'] - results['wins']:,}")
        print(f"  Win Rate:       {results['win_rate']:.2f}%")
    
    def _show_comparison(self, stay_results, switch_results):
        print("Strategy     | Games   | Wins    | Win Rate")
        print("-------------|---------|---------|----------")
        print(f"Stay         | {stay_results['total_games']:7,} | {stay_results['wins']:7,} | {stay_results['win_rate']:6.2f}%")
        print(f"Switch       | {switch_results['total_games']:7,} | {switch_results['wins']:7,} | {switch_results['win_rate']:6.2f}%")
        advantage = switch_results['win_rate'] - stay_results['win_rate']
        ratio = (switch_results['win_rate'] / stay_results['win_rate']) if stay_results['win_rate'] else float('inf')
        print(f"\nSwitch Advantage: +{advantage:.2f} percentage points")
        print(f"Switch is {ratio:.2f}x better than Stay")
    
    def _show_theoretical_comparison(self, stay_results, switch_results):
        print("Strategy | Theoretical | Actual   | Difference")
        print("---------|-------------|----------|------------")
        stay_diff = abs(stay_results['win_rate'] - self.theoretical['stay'])
        switch_diff = abs(switch_results['win_rate'] - self.theoretical['switch'])
        print(f"Stay     | {self.theoretical['stay']:8.2f}%   | {stay_results['win_rate']:6.2f}% | {stay_diff:6.2f}%")
        print(f"Switch   | {self.theoretical['switch']:8.2f}%   | {switch_results['win_rate']:6.2f}% | {switch_diff:6.2f}%")
        avg_diff = (stay_diff + switch_diff) / 2
        print(f"\nAverage deviation from theory: {avg_diff:.2f}%")
        if avg_diff < 0.5:
            print("✓ Results are very close to theoretical probabilities!")
        elif avg_diff < 1.0:
            print("✓ Results are reasonably close to theoretical probabilities.")
        else:
            print("⚠ Results deviate more than expected from theory.")
    
    def _show_conclusion(self, stay_results, switch_results):
        if switch_results['win_rate'] > stay_results['win_rate']:
            winner = "SWITCH"
            advantage = switch_results['win_rate'] - stay_results['win_rate']
        else:
            winner = "STAY"
            advantage = stay_results['win_rate'] - switch_results['win_rate']
        print(f"🎯 WINNER: {winner} strategy")
        print(f"📊 Advantage: {advantage:.2f} percentage points")
        print("\nThe Monty Hall Problem demonstrates that:")
        print("• Switching doors gives you a ~67% chance of winning")
        print("• Staying with your first choice gives you a ~33% chance")
    
    def _show_execution_stats(self, stay_results, switch_results, execution_time):
        total_games = stay_results['total_games'] + switch_results['total_games']
        gps = total_games / execution_time if execution_time > 0 else 0
        print(f"Execution Time:     {execution_time:.2f} seconds")
        print(f"Total Games:        {total_games:,}")
        print(f"Games per Second:   {gps:,.0f}")
    
    def show_quick_summary(self, stay_results, switch_results):
        print(f"Quick Results: Stay {stay_results['win_rate']:.1f}% vs Switch {switch_results['win_rate']:.1f}%")
        print("Switch strategy wins! 🎉" if switch_results['win_rate'] > stay_results['win_rate'] else "Unexpected result - Stay strategy won this time!")
