What the Program does:

The programs asks the user to select how many games to run.
If the user selected 200,000 games to simulate in the Monty Hall Problem:
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


My LLM prompts:
I would like to generate a Python code app that checks the probability of winning a car in the game of Monty Hall Problem. As I am a layman in developing and installing, every command should be clear and simple. I am working with Windows's Linux WSL, and opened a folder for this project: adarayn@Hadar-Wayn-PM:/mnt/c/2025AIDEV/L5/MontyHallProblem$ Create a Python program in which there are 3 doors. Defining randomly 3 variables. The system draws randomly where the car is 0,0,1 or 0,1,0 or 1,0,0. The system simulates a person selecting randomly one of the above options. After the person selected randomly a door, the system will open (reveal a door) without a car behind it -- and practically remove the option to select. So now the person should stay with the first door selected, or decides to select a second door. The system should run 200,000 events where a person selected randomly a door: 100,000 events where the person selected randomly a door, and stays with the first selection. 100,000 events where the person selected randomly a door, and changes the first selection to the second door. As the goal of this program is to see the probability to win a car by staying with first selection vs selecting the second door, the results should show the probability base on those 200,000 events.
The user should select how many events will be. Don't set the 200,000 events hardcoded, but after running the application, the user should be asked if to use 20, 200, 2000, 20000 or 200000 events.
Step 1: Create a PRD and include all requirements in a clear and simple manner for layman.
Step 2: Generate python code.
Notes for step 2: Don't start before I confirm the PRD. Manage the python files in a good structure. Try not to have more that 100 code lines per file. Check and validate that the progrma is working and there are no bugs.
Step 3: Generate Installation and Setup file. I want that the installation and setup of the environment will be very easy for layman. Better to run one single file with simple command like 'python main.py' or 'python3 main.py'.
Step 4: Sharing the GitHub Repository. I want to share that as a repository in my GitHub account. Generate all the commands with the WSL (do not use GitHub, only WSL) to enable me sharing a repository of that from my GitHub account: https://github.com/hadarwayn.
