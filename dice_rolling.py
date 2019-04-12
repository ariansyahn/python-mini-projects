import random


def roll():
    num_rolled = random.randint(1, 6)
    return num_rolled


def main():
    # sides = 6
    rolling = True
    while rolling:
        roll_again = input("Ready to Roll? ENTER=Roll, Q=Quit.")
        if roll_again.lower() != "q":
            num_rolled = roll()
            print("You rolled a", num_rolled)
        else:
            rolling = False
    print("Thanks for playing.")


main()
