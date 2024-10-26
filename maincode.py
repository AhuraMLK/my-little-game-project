import random
import ast
from checker import contains_only_digits,contains_only_letters
from ahoura import add_players

def help():
    while True:
        print(
            "\n \n **** Leaderboard Players Project ****\n \
    • 1. Add a player \n \
    • 2. View top 3 gamers \n \
    • 3. Search for a player \n \
    • 4. Update player information \n \
    • 5. Delete a player \n \
    • 6. Show all players \n \
    • 7. Save and Exit \n \
    • 8. play game \n"
        )
        selection = int(input("Select a number between 1 to 8: "))

        if selection == 1:
            add_players()
        elif selection == 2:
            show_top_three_gamers()
        elif selection == 3:
            search_for_player()
        # elif selection == 4:
        #     update_player()
        elif selection == 5:
            delete_player()
        elif selection == 6:
            show_all_players()
        elif selection == 7:
            save_data()
        elif selection == 8:
            play_game()
        else:
            break

def save_data():
    with open('./data/data.txt', 'w') as file_to_save:
        for player in Player_list:
            file_to_save.write(str(player) + '\n')
    print("Data saved successfully!")
    exit()

def load_data():
    try:
        with open('./data/data.txt', 'r') as file_to_read:
            data = file_to_read.readlines()
            return [ast.literal_eval(player.strip()) for player in data]
    except FileNotFoundError:
        return []

Player_list = load_data()
help()
