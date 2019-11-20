import random

def file():
    file_to_open = open("numbers.txt", "w+")
    for i in range(1,101):
        file_to_open.write(str(i) + "\n")
    file_to_open.close()
    print("Hello, I want to present you my guessing game :)")
    print("The range of numbers is between 1 - 100")


def play(number_guesses):
    lines = open("numbers.txt").read().splitlines()
    line = random.choice(lines)
    number = int(line)
    while number_guesses < 8:
        guess = int(input("Your guess: "))
        number_guesses += 1
        if guess < number:
            print("Enter higher number")
        elif guess > number:
            print("Enter lower number")
        elif guess == number:
            print("Correct, you got it!")
            return "Congratulations, you end the game :D"
    else:
        return 'Unlucky, try again :P'

def main():
    file()
    print(play(0))

main()
