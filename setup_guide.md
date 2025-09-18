# Monty Hall Problem Simulation — Installation & Setup (WSL-Friendly, Updated)

This guide keeps things **simple** and works nicely on **Windows Subsystem for Linux (WSL)**.

## 1) Go to your project folder
```bash
cd /mnt/c/2025AIDEV/L5/MontyHallProblem
```

## 2) Make sure Python 3 exists
```bash
python3 --version
```
If that errors:
```bash
sudo apt update
sudo apt install -y python3
```

## 3) Create the four Python files **with these exact names**
> The filenames must match the imports in the code.

```bash
nano main.py
```
Paste the contents of `main.py` (from the files I provided), then save with `Ctrl+X`, `Y`, `Enter`.

```bash
nano game_logic.py
```
Paste, save.

```bash
nano simulation.py
```
Paste, save.

```bash
nano results.py
```
Paste, save.

**Check they exist:**
```bash
ls -la *.py
```

## 4) Run it 🎬
```bash
python3 main.py
```
- Pick **total games** from: `20, 200, 2000, 20000, 200000`  
- The app splits them equally between **Stay** and **Switch**.
- Press Enter to start. Wait for simple 10% progress updates.
- Read the results and conclusion.

## Example snippet you’ll see
```
This simulation will test both strategies with 200,000 total games...
- Stay Strategy:   100,000 games
- Switch Strategy: 100,000 games
```

## Troubleshooting
**“No module named game_logic/simulation/results”**  
You’re probably in the wrong folder or the filenames don’t match. Do:
```bash
pwd
ls -la
```

**`python3: command not found`** → install Python (see step 2).

**Permission errors**  
```bash
chmod +x main.py
```

**Results look slightly off**  
That’s normal random variation. With larger totals (e.g., 200,000), results should be very close to theory:
- Stay ≈ 33.33%
- Switch ≈ 66.67%

## File Layout
```
MontyHallProblem/
├── main.py
├── game_logic.py
├── simulation.py
└── results.py
```
