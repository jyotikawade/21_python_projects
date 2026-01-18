name = input("type your name:  ")  
print(f"Welcome {name} to this adventure!")
answer = input("You are at a crossroad, where do you want to go? Type 'left' or 'right' \n").lower()
if answer == "left":
    answer = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if answer == "wait":
        answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if answer == "red":
            print("It's a room full of fire. Game Over.")
        elif answer == "yellow":
            print("You found the treasure! You Win!")
        elif answer == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    if answer == "right":
        answer = input("You come to a bridge. It looks wobbly. Do you want to 'cross' it or 'turn back'? \n").lower()
        if answer == "cross":
            print("The bridge collapses and you fall into a river full of crocodiles. Game Over.")
        elif answer == "turn back":
            print("You return home safely. Game Over.")
        else:
            print("You hesitate for too long and a wild animal attacks you. Game Over.")

