print("welcome to my computer quiz !")

playing = input("do you want to play ? yes/no:  ")

if playing.lower() != "yes":
    quit()

print("okay! let's play :)")
score = 0
answer = input("\nwhat does cpu stand for ? ")
if answer.lower() == "central processing unit":
    print("correct !")
    score += 1
else:
    print("incorrect !")
    print("the correct answer is 'central processing unit'")
answer = input("\nwhat does gpu stand for ? ")
if answer.lower() == "graphics processing unit":
    print("correct !")
    score += 1
else:
    print("incorrect !")
    print("the correct answer is 'graphics processing unit'")
answer = input("\nwhat does ram stand for ? ")
if answer.lower() == "random access memory":
    print("correct !")
    score += 1
else:
    print("incorrect !")
    print("the correct answer is 'random access memory'")
answer = input("\nwhat does rom stand for ? ")
if answer.lower() == "read only memory":
    print("correct !")
    score += 1
else:
    print("incorrect !")
    print("the correct answer is 'read only memory'")
answer = input("\nwhat does hdd stand for ? ")
if answer.lower() == "hard disk drive":
    print("correct !")
    score += 1
else:
    print("incorrect !")
    print("the correct answer is 'hard disk drive'")
print("\n\nyou got " + str(score) + " questions correct !")
print("\nyou got " + str((score / 5) * 100) + "%.\n")
