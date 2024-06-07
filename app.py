import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        return 'player'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        return 'player'
    elif player_choice == 'paper' and computer_choice == 'rock':
        return 'player'
    else:
        return 'computer'
    
def main():
    player_score = 0
    computer_score = 0

    while True:
        # get player choice
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        
        # validate player choice
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, please try again.")
            continue

        # get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # determine the winner
        winner = get_winner(player_choice, computer_choice)
        if winner == "player":
            print("You win!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a draw!")

        # ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    # display the final scores
    print(f"Final scores - Player: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()