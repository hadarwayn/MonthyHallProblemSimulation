#!/usr/bin/env python3
"""
Monty Hall Problem Simulation - Main Entry Point
Run this file to start the simulation and see probability results.
"""

import sys
import time
from simulation import MontyHallSimulation
from results import ResultsDisplay

ALLOWED_TOTALS = [20, 200, 2000, 20000, 200000]
DEFAULT_TOTAL = 200000

def ask_total_games():
    print("Choose how many TOTAL games to run:")
    print("  1) 20\n  2) 200\n  3) 2,000\n  4) 20,000\n  5) 200,000 (recommended)")
    raw = input(f"Enter 20 / 200 / 2000 / 20000 / 200000 (Enter = {DEFAULT_TOTAL}): ").strip()
    if not raw:
        return DEFAULT_TOTAL
    try:
        value = int(raw.replace(',', ''))
    except ValueError:
        print("Invalid input. Using default.")
        return DEFAULT_TOTAL
    if value not in ALLOWED_TOTALS:
        print("Unsupported choice. Using default.")
        return DEFAULT_TOTAL
    return value

def main():
    print("="*60)
    print("MONTY HALL PROBLEM PROBABILITY SIMULATION")
    print("="*60)
    print()
    print("The Monty Hall Problem:")
    print("- 3 doors: 1 car, 2 goats")
    print("- You pick a door")
    print("- Host opens a door with a goat")
    print("- Do you stay or switch to the other door?")
    print()

    total_games = ask_total_games()
    per_strategy = total_games // 2
    print()
    print(f"This simulation will test both strategies with {total_games:,} total games...")
    print(f"- Stay Strategy:   {per_strategy:,} games")
    print(f"- Switch Strategy: {per_strategy:,} games")
    print()

    try:
        input("Press Enter to start the simulation (or Ctrl+C to exit)...")
    except KeyboardInterrupt:
        print("\nSimulation cancelled.")
        sys.exit(0)
    
    print("\nStarting simulation...")
    print("-" * 40)
    start_time = time.time()
    
    try:
        sim = MontyHallSimulation()
        print("Running Stay Strategy simulations...")
        stay_results = sim.run_strategy_simulation("stay", per_strategy)
        print("\nRunning Switch Strategy simulations...")
        switch_results = sim.run_strategy_simulation("switch", per_strategy)
        execution_time = time.time() - start_time
        ResultsDisplay().show_results(stay_results, switch_results, execution_time)
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError during simulation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
