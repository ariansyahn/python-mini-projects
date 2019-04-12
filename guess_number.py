import random


def is_valid_num(s):
    if s.isdigit() and 1 <= int(s) <= 15:
        return True
    else:
        return False


def main():
    number = random.randint(1, 15)
    guessed_number = False
    guess = input("Guess a number between 1 and 15 : ")
    num_guesses = 0
    while not guessed_number:
        if not is_valid_num(guess):
            guess = input("MUST number between 1 and 15")
            continue
        else:
            num_guesses += 1
            guess = int(guess)

        if guess < number:
            guess = input("Too Low. Guess again : ")
        elif guess > number:
            guess = input("Too High. Guess again : ")
        else:
            print("You got it!", num_guesses, "guesses")
            guessed_number = True

    print("Thanks for playing!")


main()
