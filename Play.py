import random


def play(n):
    global guess
    count = 0
    computer = random.randint(1, n)
    print(f"Let's play a game of Guessing Game!\nI am guessing a number beetween 1 and {n}\n......")
    print("Your turn now.")
    while count < (n/2):
        guess = int(input(f"Guess a number between 1 and {n}:\n"))
        count += 1
        if guess < computer:
            print("Your guess is too low!")
        elif guess > computer:
            print("Your guess is too high!")
        else:
            break
    if guess == computer:
        print("Congrats! You guessed my number in " + str(count) + " tries!\nYou won!")
    else:
        print(f"Sorry, you didn't guess my number in less then {n/2} tries!\nYou lost!")
