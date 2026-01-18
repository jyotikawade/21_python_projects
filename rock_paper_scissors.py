import random

user_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]
def get_computer_choice():
    return random.choice(choices)
def get_user_choice():
    while True:
        user_input = input("Enter rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")
def determine_winner(user_choice, computer_choice):
    global user_wins, computer_wins
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_wins += 1
        return "You win this round!"
    else:
        computer_wins += 1
        return "Computer wins this round!"
def play_game():
    rounds = 5
    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print(f"Score -> You: {user_wins}, Computer: {computer_wins}")
    if user_wins > computer_wins:
        print("\nCongratulations! You won the game!")
    elif computer_wins > user_wins:
        print("\nComputer wins the game! Better luck next time.")
    else:
        print("\nThe game is a tie!")
if __name__ == "__main__":
    play_game()