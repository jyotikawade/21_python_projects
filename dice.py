import random


def roll_dice():
    return random.randint(1, 6)


# ----------- GET NUMBER OF PLAYERS -----------
while True:
    players = input("Enter the number of players (2 - 4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid input. Please enter a number.")


# ----------- GAME SETUP -----------
WINNING_SCORE = 50
player_scores = [0] * players


# ----------- MAIN GAME LOOP -----------
turn = 0
while turn < 5:

    for player_idx in range(players):
        print(f"\n🎲 Player {player_idx + 1}'s turn")
        print("Total score:", player_scores[player_idx])

        current_score = 0
        rolled_once = False   # 👈 important fix

        while True:
            should_roll = input("Roll the dice? (y/n): ").lower()

            # Force at least one roll
            if should_roll != "y":
                if not rolled_once:
                    print("You must roll at least once!")
                    continue
                break

            rolled_once = True
            value = roll_dice()
            print("You rolled:", value)

            if value == 1:
                print("Rolled a 1! Turn over 😢")
                current_score = 0
                break
            else:
                current_score += value
                print("Current turn score:", current_score)
        turn += 1

        # Add current score to total score
        player_scores[player_idx] += current_score
        print("Total score now:", player_scores[player_idx])

        # Stop game immediately if someone wins
        if player_scores[player_idx] >= WINNING_SCORE:
            break


# ----------- WINNER DECLARATION -----------
winning_score = max(player_scores)
winner_index = player_scores.index(winning_score)

print("\n🏆 Player", winner_index + 1,
      "wins with a score of", winning_score)

