name = input("Type your name: ")
print(f"\nWelcome {name} to this adventure!")
print("Your mission is to survive and find the treasure.\n")

answer = input(
    "You are at a crossroad. Where do you want to go?\n"
    "Type 'left' or 'right': "
).lower()

# ---------------- LEFT PATH ----------------
if answer == "left":
    answer = input(
        "\nYou come to a lake. The water is dark and cold.\n"
        "There is an island in the middle.\n"
        "Type 'wait' to wait for a boat or 'swim' to swim across: "
    ).lower()

    if answer == "wait":
        answer = input(
            "\nA boat arrives safely.\n"
            "You reach the island unharmed.\n"
            "There is a house with 3 doors: red, yellow, and blue.\n"
            "Which color do you choose? "
        ).lower()

        if answer == "red":
            print("\nThe room is full of fire.")
            print("You are burned alive. 🔥 Game Over.")

        elif answer == "yellow":
            answer = input(
                "\nYou enter a golden hall full of light.\n"
                "You see a chest and a staircase.\n"
                "Type 'open chest' or 'climb stairs': "
            ).lower()

            if answer == "open chest":
                print("\nThe chest contains the hidden treasure!")
                print("🏆 Congratulations! You Win!")

            elif answer == "climb stairs":
                print("\nA trapdoor opens under your feet.")
                print("You fall into darkness. Game Over.")

            else:
                print("\nYou hesitate too long.")
                print("The hall collapses. Game Over.")

        elif answer == "blue":
            answer = input(
                "\nYou enter a dark room full of growling sounds.\n"
                "Do you want to 'fight' or 'run'? "
            ).lower()

            if answer == "fight":
                print("\nThe beasts are too strong.")
                print("You are defeated. Game Over.")

            elif answer == "run":
                print("\nYou escape safely back to the lake.")
                print("But the boat is gone. Game Over.")

            else:
                print("\nYou freeze in fear.")
                print("The beasts attack you. Game Over.")

        else:
            print("\nYou chose a door that doesn't exist.")
            print("The house collapses. Game Over.")

    elif answer == "swim":
        print("\nYou try to swim across the lake.")
        print("An angry trout attacks you. 🐟 Game Over.")

    else:
        print("\nYou stand confused and fall into the lake.")
        print("Game Over.")

# ---------------- RIGHT PATH ----------------
elif answer == "right":
    answer = input(
        "\nYou come to an old wooden bridge.\n"
        "It looks wobbly and dangerous.\n"
        "Type 'cross' or 'turn back': "
    ).lower()

    if answer == "cross":
        answer = input(
            "\nYou carefully step onto the bridge.\n"
            "Halfway across, you hear cracking sounds.\n"
            "Do you want to 'run' or 'go slow'? "
        ).lower()

        if answer == "run":
            print("\nThe bridge collapses!")
            print("You fall into a river full of crocodiles. 🐊 Game Over.")

        elif answer == "go slow":
            print("\nYou safely reach the other side.")
            answer = input(
                "\nYou see a cave and a forest.\n"
                "Type 'cave' or 'forest': "
            ).lower()

            if answer == "cave":
                print("\nA sleeping dragon wakes up.")
                print("You are burned by fire. 🔥 Game Over.")

            elif answer == "forest":
                answer = input(
                    "\nYou find a sword stuck in a stone.\n"
                    "Do you want to 'pull sword' or 'ignore'? "
                ).lower()

                if answer == "pull sword":
                    print("\nYou pull the sword successfully!")
                    print("You are now a hero.")
                    print("🏆 You Win!")

                elif answer == "ignore":
                    print("\nYou walk deeper into the forest.")
                    print("You get lost forever. Game Over.")

                else:
                    print("\nYou wait too long.")
                    print("A wild animal attacks you. Game Over.")

            else:
                print("\nYou wander aimlessly.")
                print("Game Over.")

        else:
            print("\nYou freeze in fear.")
            print("The bridge collapses. Game Over.")

    elif answer == "turn back":
        print("\nYou return home safely.")
        print("Sometimes survival is the real victory.")
        print("Game Over.")

    else:
        print("\nYou hesitate for too long.")
        print("A wild animal attacks you. Game Over.")

# ---------------- INVALID INPUT ----------------
else:
    print("\nInvalid choice.")
    print("You stand still until night falls.")
    print("Game Over.")
