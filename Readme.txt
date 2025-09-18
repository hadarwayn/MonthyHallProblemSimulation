What the Program does:

Simulate 200,000 games of the Monty Hall Problem
100,000 games where player stays with first choice
100,000 games where player switches doors
Show win percentages for both strategies
Prove that switching gives ~66.67% win rate vs ~33.33% for staying

Key Features:

✅ Random car placement (1,0,0 or 0,1,0 or 0,0,1)
✅ Random player door selection
✅ Host always opens a goat door (following game rules)
✅ Two strategies: Stay vs Switch
✅ Statistical analysis with clear results
✅ Single command execution: python3 main.py

Technical Approach:

Modular Python code (4 files, each <100 lines)
Uses only Python standard library (no external dependencies)
Fast execution (<30 seconds for 200,000 games)
Clear, formatted output showing probability results

File Structure:

main.py - Entry point
game_logic.py - Individual game mechanics
simulation.py - Run multiple games
results.py - Display formatted results

The simulation  demonstrates the famous counterintuitive result: switching doors gives you 2x better odds of winning the car!