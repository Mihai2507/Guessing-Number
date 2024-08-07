from Play import play

if __name__ == '__main__':
    print("Welcome to Guessing Game!")
    name = input("Please, enter your name:\n")
    print(f"Hello, {name}!")
    n = int(input("Please, enter the maximum number for the range:\n"))
    play(n)
