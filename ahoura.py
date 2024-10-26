from checker import contains_only_digits,contains_only_letters
from maincode import Player_list
import random

def show_all_players():
    for player in Player_list:
        print("\n\n ***", player, "***")

def add_players():
    New_Player_UserName = input("**Enter your username**\n ")
    if not contains_only_letters(New_Player_UserName):
        print("**The entered username is not valid**\n")
        return

    Player_Number_ID = input("**Enter your numeric account ID!**\n")
    if not contains_only_digits(Player_Number_ID): 
        print("**The account ID should only contain digits.**")
        Player_Number_ID = input("**Please enter a valid numeric ID!**\n")

    player_age = input("**Enter your age**\n")
    if not contains_only_digits(player_age):
        print("The entered age is not valid")
        return

    player_Bio = input("**Write a bio for your account. Bio is mandatory in this app!**\n")

    player = {
        "New_Player_UserName": New_Player_UserName,
        "Player_Number_ID": Player_Number_ID,
        "player_age": player_age,
        "player_Bio": player_Bio,
        "player_score": 0,
    }
    Player_list.append(player)
    print("*** New player added! Enjoy the game. ***")

def search_for_player():
    search_id = input("**Enter the Player ID or Username to search**\n ")

    for player in Player_list:
        if player["Player_Number_ID"] == search_id or player["New_Player_UserName"] == search_id:
            print("Player found!")
            print("ID:", player["Player_Number_ID"])
            print("Username:", player["New_Player_UserName"])
            print("Number ID:", player["Player_Number_ID"])
            print("Age:", player["player_age"])
            print("Bio:", player["player_Bio"])
            return

    print("No player found with the entered ID or Username.")

def show_top_three_gamers():
    sorted_players = sorted(Player_list, key=lambda x: int(x["player_score"]))
    print("\n*** Top 3 Players ***")
    for i, player in enumerate(sorted_players[:3], 1):
        print(f"{i}. {player['New_Player_UserName']} - score: {player['player_score']}")

def delete_player():
    search_id = input("Enter the Player ID or Username of the player to delete: ")

    for player in Player_list:
        if player["Player_Number_ID"] == search_id or player["New_Player_UserName"] == search_id:
            Player_list.remove(player)
            print(f"Player {player['New_Player_UserName']} has been deleted.")
            return

    print("No player found with the entered ID or Username.")

def play_game():
    random_number = random.randint(1, 100)
    username = input("Enter your username: ")
    print(random_number)

    for player in Player_list:
        if player["New_Player_UserName"] == username:
            print("Username found! Let's play.")
            score = 1

            while True:
                guess = input("Enter a number between 1 and 100: ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess == random_number:
                        print("Correct! You win.")
                        player['player_score'] = score
                        break
                    elif guess < random_number:
                        score += 1
                        print("Too low, try again.")
                    else:
                        score += 1
                        print("Too high, try again.")
                else:
                    print("Please enter a valid number.")
            return

    print("Username not found.")
