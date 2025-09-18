# Monty Hall Problem Simulation — PRD (Updated)

## 1. Product Overview
**Product Name:** Monty Hall Problem Probability Simulator  
**Purpose:** A Python simulation to demonstrate and calculate the probability of winning a car in the Monty Hall Problem by comparing two strategies: **staying** with the first choice vs. **switching** doors.

**Target Users:** Students, educators, and anyone curious about probability and statistics who wants to understand the counterintuitive nature of the Monty Hall Problem.

## 2. Problem Explanation (Plain Language)
There are 3 doors. One door hides a **car** (the prize); the other two hide **goats**.  
You pick a door. The **host**, who knows where the car is, opens **one of the other doors** that he knows has a goat.  
Now you may **stay** with your original door, or **switch** to the other unopened door.  
The classic question: **Is switching better?** (Yes, in theory: switching wins ~2/3 of the time.)

## 3. Simulation Requirements
### 3.1 Core Functionality
- Represent the doors as a list of three binary values like `[0, 0, 1]`, where `1` means the car and `0` means a goat.  
- Randomly place the car behind one of the doors each game.
- The player makes a random initial choice (door index 0, 1, or 2).
- The host opens a door that:
  - Is **not** the player's original choice, and
  - Has a **goat** (never the car).
- Two strategies:
  - **Stay:** keep the first chosen door.
  - **Switch:** switch to the only other unopened door.

### 3.2 Simulation Parameters
- **Total games** are selected by the user **at program start** from this set:  
  `20, 200, 2000, 20000, 200000` (default is `200000` if the user presses Enter).
- The total will be split **equally** between strategies: half for **Stay**, half for **Switch**.  
  Example: `200000` total → `100000` stay + `100000` switch.

### 3.3 Output Requirements
- Show, for each strategy:
  - Total games, number of wins, and win rate (percentage with two decimals).
- Show a side-by-side comparison and a short conclusion (which strategy won and by how much).
- Show a “theoretical vs. actual” comparison using `Stay ≈ 33.33%`, `Switch ≈ 66.67%`.
- Console output must be **clear and readable** for non-developers.

## 4. Technical Specifications
### 4.1 Programming Requirements
- **Language:** Python 3 (standard library only: `random`, `time`).
- **Structure:** Modular, separate files (keep each file under ~100 lines):
  - `main.py`: application entry point & user prompts
  - `game_logic.py`: one game mechanics
  - `simulation.py`: multiple games + progress
  - `results.py`: formatting and printing results

### 4.2 Data Structures
- Door configuration: list of three ints (0 or 1).
- Player choice, host-opened door, remaining door: ints (0–2).
- Result: boolean for win/loss.

## 5. User Experience
### 5.1 Flow
1. User runs `python3 main.py`.
2. The app briefly explains the Monty Hall Problem.
3. The app asks the user to choose **total games** from the set above (or press Enter for default `200000`).
4. The app runs half the games with **Stay** and half with **Switch**, showing a simple progress indicator.
5. The app prints the results, the theory comparison, and a short conclusion.

### 5.2 Example Output (abridged)
```
MONTY HALL SIMULATION RESULTS
STAY STRATEGY:   Total 100,000 | Wins 33,342 | Win Rate 33.34%
SWITCH STRATEGY: Total 100,000 | Wins 66,658 | Win Rate 66.66%

Switch Advantage: +33.32 percentage points
WINNER: SWITCH
```

## 6. Functional Requirements
- FR-1..FR-6: Game rules enforced (host never opens the car / player’s door; exactly one car).
- **FR-7:** Prompt the user to choose total games from `20, 200, 2000, 20000, 200000` (Enter = `200000`).
- **FR-8:** Split total games **equally** between Stay and Switch.
- **FR-9:** Compute win counts and win rates per strategy.
- **FR-10:** Display comparison and conclusion.

## 7. Non‑Functional Requirements
- Performance: `200,000` total simulations should complete in under ~30 seconds on typical WSL setups.
- Usability: One‑command run (`python3 main.py`) with friendly prompts.
- No external dependencies beyond Python’s standard library.

## 8. Installation Requirements
- Platform: WSL (Ubuntu or similar) with Python 3.6+.
- Files live in a single folder. No package managers or virtualenv required for this small project.

## 9. Success Criteria
- Switching ≈ 66.67% and Staying ≈ 33.33% (within normal random variation).
- Clear, simple user prompts and readable results.

## 10. Mathematical Background (Short)
- First pick is correct with probability `1/3`.
- The other two doors combined have probability `2/3` of hiding the car.  
- When the host removes one goat door, the entire `2/3` probability “moves” to the remaining unopened door, so **switching** is better.
