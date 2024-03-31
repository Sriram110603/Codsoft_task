import random
choices = ["rock", "paper", "scissors"]
def get_computer_choice():
       return random.choice(choices)
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice not in choices:
            print("Invalid choice. Enter your choice (rock/paper/scissors): ")
        else:
            return choice

def determine_winner(player_choice, computer_choice):
   
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (
        player_choice == "paper" and computer_choice == "rock"
    ) or (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    player_points = 0
    computer_points = 0
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Player chose {player_choice}, computer chose {computer_choice}.")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        if "Player wins!" in result:
            player_points += 1
        elif "Computer wins!" in result:
            computer_points += 1
        print(f"Player points: {player_points}, Computer points: {computer_points}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
if __name__ == "__main__":
    play_game()

