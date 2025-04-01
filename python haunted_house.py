import random
import time

# Game state class to manage all game variables
class GameState:
    def __init__(self):
        self.inventory = []  # List to store collected items (keys, holy water, medkit)
        self.current_room = "foyer"  # Starting room
        self.ghost_room = random.choice(["kitchen", "library", "attic"])  # Ghost starts in a random room
        self.health = 100  # Player's starting health points
        # Dictionary defining all rooms with descriptions, exits, keys, traps, and items
        self.rooms = {
            "foyer": {"desc": "A dusty foyer with creaky floorboards. Exits: north, east.", 
                     "exits": {"north": "kitchen", "east": "library"}, "key": None, "trap": "falling chandelier", "item": None},
            "kitchen": {"desc": "A rusty kitchen with broken cabinets. Exits: south, west.", 
                       "exits": {"south": "foyer", "west": "basement"}, "key": "silver key", "trap": None, "item": "holy water"},
            "library": {"desc": "An old library with tattered books. Exits: west, north.", 
                       "exits": {"west": "foyer", "north": "attic"}, "key": "gold key", "trap": "hidden pit", "item": None},
            "basement": {"desc": "A damp basement with cobwebs. Exits: east, up.", 
                        "exits": {"east": "kitchen", "up": "attic"}, "key": "rusty key", "trap": None, "item": "medkit"},
            "attic": {"desc": "A creepy attic with a locked door to freedom. Exits: south, down.", 
                     "exits": {"south": "library", "down": "basement"}, "key": None, "trap": None, "item": None}
        }
        self.game_over = False  # Flag to track if game has ended
        self.turn_count = 0  # Counter for player actions to trigger ghost movement
        self.ghost_stunned = False  # Flag to track if ghost is temporarily stunned

# Create a global game instance
game = GameState()

# Function to print text slowly for dramatic effect
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)  # Print character without newline, flush to display immediately
        time.sleep(0.03)  # Small delay between characters
    print()  # Newline at the end

# Function to handle ghost movement and potential encounters
def move_ghost():
    global game
    game.turn_count += 1  # Increment turn counter with each player action
    if game.ghost_stunned:  # If ghost is stunned, it skips this turn
        game.ghost_stunned = False
        print_slow("The ghost recovers from the holy water!")
        return
    if game.turn_count % 3 == 0:  # Ghost moves every 3 turns
        possible_rooms = [room for room in game.rooms if room != game.current_room and room != game.ghost_room]
        if possible_rooms:  # Ensure there are rooms to move to
            game.ghost_room = random.choice(possible_rooms)  # Move ghost to a random valid room
            if game.current_room == game.ghost_room:
                ghost_encounter()  # Trigger encounter if ghost moves into player's room

# Function to handle ghost attack or stun
def ghost_encounter():
    global game
    if "holy water" in game.inventory:  # Check if player has holy water to stun ghost
        print_slow("The ghost lunges at you! You splash it with holy water, stunning it!")
        game.inventory.remove("holy water")  # Remove used holy water
        game.ghost_stunned = True  # Stun ghost for one turn
    else:  # If no holy water, ghost attacks
        damage = random.randint(20, 40)  # Random damage between 20-40 HP
        game.health -= damage
        print_slow(f"The ghost attacks you, dealing {damage} damage! HP: {game.health}")
        if game.health <= 0:  # Check if player dies
            print_slow("The ghost’s icy grip overwhelms you. You’re dead!")
            game.game_over = True

# Function to check and trigger room traps
def check_trap():
    room = game.rooms[game.current_room]
    if room["trap"] and random.random() < 0.3:  # 30% chance to trigger trap if present
        if room["trap"] == "falling chandelier":
            print_slow("A chandelier crashes down from above!")
            damage = random.randint(10, 30)  # Random damage between 10-30 HP
            game.health -= damage
            print_slow(f"You take {damage} damage! HP: {game.health}")
        elif room["trap"] == "hidden pit":
            print_slow("You step into a hidden pit!")
            damage = random.randint(15, 35)  # Random damage between 15-35 HP
            game.health -= damage
            print_slow(f"You fall and take {damage} damage! HP: {game.health}")
        if game.health <= 0:  # Check if trap kills player
            print_slow("The trap proves fatal. You’re dead!")
            game.game_over = True

# Function to look around the current room
def look():
    room = game.rooms[game.current_room]
    print_slow(room["desc"])  # Display room description
    if room["key"] and room["key"] not in game.inventory:
        print_slow(f"You see a {room['key']} on the floor.")  # Show key if present and not taken
    if room["item"] and room["item"] not in game.inventory:
        print_slow(f"You spot a {room['item']} in the corner.")  # Show item if present and not taken
    print_slow(f"Your health: {game.health} HP")  # Display current health

# Function to move between rooms
def move(direction):
    room = game.rooms[game.current_room]
    if direction in room["exits"]:  # Check if direction is a valid exit
        game.current_room = room["exits"][direction]
        print_slow(f"You move to the {game.current_room}.")
        look()  # Show new room details
        check_trap()  # Check for traps in new room
        move_ghost()  # Update ghost position
        if game.current_room == game.ghost_room and not game.ghost_stunned:
            ghost_encounter()  # Trigger encounter if ghost is present and not stunned
    else:
        print_slow("You can’t go that way!")

# Function to pick up items or keys
def take():
    room = game.rooms[game.current_room]
    if room["key"] and room["key"] not in game.inventory:  # Check for key
        game.inventory.append(room["key"])
        print_slow(f"You picked up the {room['key']}.")
    elif room["item"] and room["item"] not in game.inventory:  # Check for item
        game.inventory.append(room["item"])
        print_slow(f"You picked up the {room['item']}.")
    else:
        print_slow("There’s nothing to take here.")
    move_ghost()  # Ghost moves after taking an action

# Function to use items from inventory
def use():
    if not game.inventory:  # Check if inventory is empty
        print_slow("You have nothing to use!")
        return
    usable_items = [item for item in game.inventory if item not in ["silver key", "gold key", "rusty key"]]
    print_slow("You can use: " + ", ".join(usable_items))  # Show usable items
    item = input("What do you want to use? ").strip().lower()
    if item == "medkit" and item in game.inventory:  # Use medkit to heal
        heal = random.randint(30, 50)
        game.health = min(100, game.health + heal)  # Cap health at 100
        game.inventory.remove("medkit")
        print_slow(f"You use the medkit, restoring {heal} HP! Current HP: {game.health}")
    elif item == "holy water" and item in game.inventory and game.current_room == game.ghost_room:  # Use holy water on ghost
        print_slow("You splash the ghost with holy water, stunning it!")
        game.inventory.remove("holy water")
        game.ghost_stunned = True
    else:
        print_slow("You can’t use that now!")  # Invalid item or context
    move_ghost()  # Ghost moves after using an item

# Function to check inventory contents
def check_inventory():
    if game.inventory:
        print_slow("You have: " + ", ".join(game.inventory))  # List all items
    else:
        print_slow("Your inventory is empty.")
    print_slow(f"Your health: {game.health} HP")  # Show health status

# Function to attempt escape from the attic
def escape():
    if game.current_room == "attic":  # Must be in attic to escape
        required_keys = ["silver key", "gold key", "rusty key"]
        if all(key in game.inventory for key in required_keys):  # Check for all keys
            print_slow("You use all three keys to unlock the door. You escape the haunted house!")
            game.game_over = True
            return True
        else:
            print_slow("You need all three keys (silver, gold, rusty) to unlock the door!")
    else:
        print_slow("You can only escape from the attic!")
    return False

# Main game loop
def main():
    print_slow("Welcome to the Haunted House!")
    print_slow("Find the silver, gold, and rusty keys to escape the attic.")
    print_slow("Beware traps and the ghost—use items wisely to survive!")
    print_slow("Commands: look, move <direction>, take, use, inventory, escape, quit")
    look()  # Initial room description

    while not game.game_over:  # Continue until game ends
        command = input("> ").strip().lower().split()  # Get player input
        if not command:  # Skip empty input
            continue
        
        action = command[0]
        if action == "quit":  # Exit game
            print_slow("You abandon your escape attempt...")
            break
        elif action == "look":  # Look around
            look()
        elif action == "move" and len(command) > 1:  # Move in a direction
            move(command[1])
        elif action == "take":  # Pick up item/key
            take()
        elif action == "use":  # Use an item
            use()
        elif action == "inventory":  # Check inventory
            check_inventory()
        elif action == "escape":  # Try to escape
            if escape():
                print_slow("Congratulations! You’ve survived!")
        else:
            print_slow("Invalid command. Try: look, move <direction>, take, use, inventory, escape, quit")

    if game.game_over and game.current_room != "attic":  # Check for loss condition
        print_slow("Game Over! You didn’t make it out alive.")

# Start the game if run as main script
if __name__ == "__main__":
    main()