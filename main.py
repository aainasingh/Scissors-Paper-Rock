import random

# words
# select s p r
# computer generate s p r
# way to compare them
# who wins/ties
# human vs computer
# bo3

winner = None

game_still_going = True

player = None

computer = None


def player_choice():
    global player
    player = input("Choose one from Scissors, Paper or Rock: ").capitalize()

    return

def computer_choice():
    global computer
    computer_choices = ["Scissors", "Paper", "Rock"]

    computer = random.choice(computer_choices)
    return computer

def check_who_wins(player_choice, computer_choice):
    
    global winner
    global game_still_going

    win_condition = {
        "Scissors": "Paper",
        "Paper": "Rock",
        "Rock": "Scissors"
    }
    
    if player_choice == "Scissors" and computer_choice == win_condition[player_choice]:
        winner = "Player"
    elif player_choice == "Paper" and computer_choice == win_condition[player_choice]:
        winner = "Player"
    elif player_choice == "Rock" and computer_choice == win_condition[player_choice]:
        winner = "Player"
    elif computer_choice == "Scissors" and player_choice == win_condition[computer_choice]:
        winner = "Computer"
    elif computer_choice == "Paper" and player_choice == win_condition[computer_choice]:
        winner = "Computer"
    elif computer_choice == "Rock" and player_choice == win_condition[computer_choice]:
        winner = "Computer"
    else:
        winner = None


def play_game():
    
    global game_still_going
    global player

    while game_still_going:
        player_choice()
        if player not in ["Scissors", "Paper", "Rock"]:
            print("Invalid input! Try again.")
        else:
            game_still_going = False
    
    
    print("The Computer chose: " + computer_choice())
    check_who_wins(player, computer)

    if winner == None:
        print("No one won!")
    elif winner == "Player" or winner == "Computer":
        print(winner + " won!")
    

play_game()
