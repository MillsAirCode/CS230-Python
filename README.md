# Haunted House Action Game

## Overview
This is a text-based Python game where you explore a haunted house, collect keys to escape, and survive traps and ghost encounters. Created as an action-packed adventure, you must manage your health, use items strategically, and avoid deadly hazards to make it out alive.

## Features
- **Dynamic Exploration**: Navigate through 5 interconnected rooms (foyer, kitchen, library, basement, attic).
- **Key Collection**: Find the silver, gold, and rusty keys to unlock the attic door and escape.
- **Health System**: Start with 100 HP; traps and ghost attacks reduce your health.
- **Traps**: Encounter a falling chandelier (foyer) or hidden pit (library) with a 30% trigger chance, dealing variable damage.
- **Items**:
  - **Holy Water** (kitchen): Stun the ghost for one turn to avoid an attack.
  - **Medkit** (basement): Restore 30-50 HP.
- **Ghost Threat**: The ghost moves every 3 turns and attacks for 20-40 damage unless stunned.
- **Interactive Commands**: Use `look`, `move`, `take`, `use`, `inventory`, `escape`, and `quit` to play.

## Requirements
- Python 3.x
- No external libraries beyond the standard `random` and `time` modules.

## How to Play
1. **Run the Game**:
   - **Local**: Save the code as `haunted_house_action.py` and run it with:
     ```bash
     python haunted_house_action.py
     ```
   - **Pyodide**: Paste the code into a Pyodide-compatible environment (e.g., Pyodide console or Jupyter notebook) and execute it.
2. **Game Start**: You begin in the foyer with 100 HP. The goal is to escape from the attic.
3. **Commands**:
   - `look`: View the room description, items, and your health.
   - `move <direction>`: Move to another room (e.g., `move north`, `move up`).
   - `take`: Pick up a key or item in the room.
   - `use`: Use an item (e.g., type `medkit` or `holy water` when prompted).
   - `inventory`: Check your items and health.
   - `escape`: Attempt to escape (only works in the attic with all 3 keys).
   - `quit`: Exit the game.
4. **Survival Tips**:
   - Watch your HP—use the medkit if it drops too low.
   - Stun the ghost with holy water if it appears in your room.
   - Move carefully to avoid triggering traps.
5. **Win Condition**: Reach the attic with all 3 keys and use `escape`.
6. **Lose Condition**: HP reaches 0 from traps or ghost attacks.

## Game Mechanics
- **Rooms**: Each room has exits, and some contain keys, items, or traps.
- **Ghost**: Moves every 3 player actions to a random room (not the player’s current room or its own previous room). Attacks if it lands in your room unless stunned.
- **Traps**: Trigger randomly (30% chance) when entering a room with a trap, dealing damage:
  - Falling Chandelier: 10-30 HP
  - Hidden Pit: 15-35 HP
- **Items**:
  - Holy Water: Single-use, stuns the ghost for one turn.
  - Medkit: Single-use, heals 30-50 HP (max 100 HP).

## Code Structure
- **GameState Class**: Manages inventory, current room, ghost location, health, and game status.
- **Functions**:
  - `print_slow`: Displays text with a slow, dramatic effect.
  - `move_ghost`: Handles ghost movement and encounters.
  - `ghost_encounter`: Manages ghost attacks or stunning.
  - `check_trap`: Triggers and resolves trap effects.
  - `look`, `move`, `take`, `use`, `inventory`, `escape`: Core player actions.
  - `main`: Runs the game loop.

## Example Gameplay
```
Welcome to the Haunted House!
Find the silver, gold, and rusty keys to escape the attic.
Beware traps and the ghost—use items wisely to survive!
Commands: look, move <direction>, take, use, inventory, escape, quit
You're in a dusty foyer with creaky floorboards. Exits: north, east.
Your health: 100 HP
> move north
You move to the kitchen.
A rusty kitchen with broken cabinets. Exits: south, west.
You see a silver key on the floor.
You spot a holy water in the corner.
Your health: 100 HP
> take
You picked up the silver key.
> take
You picked up the holy water.
> move west
You move to the basement.
A damp basement with cobwebs. Exits: east, up.
You see a rusty key on the floor.
You spot a medkit in the corner.
Your health: 100 HP
```

## Troubleshooting
- **No Output**: Ensure you’ve executed the code fully in your environment.
- **Errors**: If running in Pyodide, paste only the Python code (no surrounding text).
- **Stuck?**: Type `quit` to exit and restart.

## Credits
- Created by: Brad Mills ([@MillsAirCode](https://github.com/MillsAirCode))
- Purpose: An action-enhanced text adventure for Python enthusiasts.

Enjoy the thrill of escaping the haunted house!
