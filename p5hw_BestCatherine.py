# Catherine Best
# 4/30/2025
# P5HW
# Character Creation Game


import random

def create_character():
    print("\n Create your character")
    name = input("Enter character name: ")
    health = int(input("Enter health points (1-100): "))
    attack = int(input("Enter attack points (1-50): "))
    magic = int(input("Enter magic points (1-50): "))

    character = {
        "name": name,
        "health": health,
        "attack": attack,
        "magic": magic
    }

    return character

def display_character(character):
    print("\n Character Stats")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")


def battle(character):
    print("\n Battle Encounter!")
    enemy_attack = random.randint(5, 20)
    character["health"] -= enemy_attack
    print(f"You were attacked and lost {enemy_attack} health points!")

def find_item(character):
    print("\n You found a magical potion!")
    bonus = random.randint(5, 15)
    character["magic"] += bonus
    print(f"You gained {bonus} magic points!")

def go_on_quest(character):
    print("\n You are going on a quest...")
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        gain = random.randint(10, 20)
        character["attack"] += gain
        print(f"You successfully completed the quest and gained {gain} attack points!")
    else:
        loss = random.randint(5, 15)
        character["health"] -= loss
        print(f"You failed the quest and lost {loss} health points!")

def main():
    characters = []

    while True:
        print("\n Welcome to the Character Creation Game!")
        print("1. Create a new character")
        print("2. Display all characters")
        print("3. Go on an adventure")
        print("4. Exit game")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            character = create_character()
            characters.append(character)
            print(" Character created successfully!")

        elif choice == "2":
            if not characters:
                print(" No characters created yet.")
            else:
                for i, char in enumerate(characters):
                    print(f"\nCharacter {i+1}")
                    display_character(char)

        elif choice == "3":
            if not characters:
                print(" Create a character first!")
                continue

            for char in characters:
                print(f"\n What should {char['name']} do?")
                print("a. Battle")
                print("b. Find Item")
                print("c. Go on Quest")
                action = input("Choose action (a/b/c): ").lower()

                if action == "a":
                    battle(char)
                elif action == "b":
                    find_item(char)
                elif action == "c":
                    go_on_quest(char)
                else:
                    print("Invalid action.")

                if char["health"] <= 0:
                    print(f" {char['name']} has no health left. Game over for this character!")
                    characters.remove(char)

        elif choice == "4":
            print(" Exiting the game. Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")


main()
