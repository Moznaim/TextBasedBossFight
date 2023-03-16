from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
import random

# Function to get player input and create player objects
def create_player():
    print("Choose your class:")
    print("1 - Novice")
    print("2 - Swordsman")
    print("3 - Archer")
    print("4 - Magician")
    class_choice = input("Enter your choice: ")
    username = input("Enter your username: ")
    if class_choice == "1":
        player = Novice(username)
    elif class_choice == "2":
        player = Swordsman(username)
    elif class_choice == "3":
        player = Archer(username)
    elif class_choice == "4":
        player = Magician(username)
    return player

# Function to simulate the game
def game():
    print("Welcome to the Boss Battle Game!")
    players = []
    solo = input("Do you want to play solo or with two persons? (solo/two): ")
    if solo == "solo":
        players.append(create_player())
    elif solo == "two":
        players.append(create_player())
        players.append(create_player())
    else:
        print("Invalid input. Exiting game.")
        return
    boss = Boss("The Boss")
    print(f"{boss.getUsername()} appears! Boss HP: {boss.getHp()}")
    turn = 1

    while boss.getHp() > 0:
        print(f"\n--- Turn {turn} ---")
        for player in players:
            print(f"\n{player.getUsername()}'s turn:")
            action_choice = input("Choose your action (1 - Basic Attack, 2 - Special Attack): ")
            print(f"{player.getUsername()}'s HP: {player.getHp()} ")
            if action_choice == "1":
                player.basicAttack(boss)
            elif action_choice == "2":
                if isinstance(player, Swordsman):
                    player.slashAttack(boss)
                elif isinstance(player, Archer):
                    player.rangedAttack(boss)
                elif isinstance(player, Magician):
                    player.heal(player)
            if boss.getHp() <= 0:
                break

        if boss.getHp() > 0:
            print(f"\n{boss.getUsername()}'s turn:")
            boss.decimatingSmash(random.choice(players))
            print(f"Boss HP: {boss.getHp()}")
            for player in players:
                if player.getHp() <= 0:
                    print(f"\n--- {player.getUsername()} has been defeated! ---")
                    return

        turn += 1
    print(f"\n--- {boss.getUsername()} has been defeated! ---")
    for player in players:
        print(f"{player.getUsername()} HP: {player.getHp()}")

# Call the game function
game()
