import random


def play():
    global guess
    count = 0
    computer = random.randint(1, 10)
    print("Let's play a game of Guessing Game!\nI am guessing a number beetween 1 and 10\n")
    while count < 5:
        guess = int(input("Guess a number between 1 and 10:\n"))
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
        print("Sorry, you didn't guess my number in less then 5 tries!\nYou lost!")


if __name__ == '__main__':
    print("Welcome to Guessing Game!")
    name = input("Please, enter your name:\n")
    print(f"Hello, {name}!")
    play()
