import random


class Hangman:
    def __init__(self, word):
        self.word = word
        self.letters = ""

    @staticmethod
    def file_with_words():
        list_of_words = ["home", "dragon", "cake", "computer", 'room', 'bathroom']
        file = open('words.txt', 'w+')
        for element in list_of_words:
            file.write(str(element) + '\n')
        file.close()

    @staticmethod
    def read_words():
        list_of_words = []
        with open('words.txt', 'r') as f:
            for x in f.read().split():
                list_of_words.append(x)
        return list_of_words

    @staticmethod
    def hello():
        name = input('Enter your name: ')
        print('Hello ' + name + ' welcome into my Hangman Game :D')
        print("You've got 10 chances to guess the word so good luck and have fun :D")

    @property
    def grid(self):
        grid = ""
        for l in self.word:
            if l in self.letters:
                grid += l
            else:
                grid += ' _ '
        return grid

    def show_grid(self):
        print('Grid: ' + self.grid)
        print('Your choose: ' + self.letters)

    def ask_letter(self):
        same_letter = False
        guess = input('Guess a letter: ')
        letter = guess.lower()
        if letter in self.letters:
            print('Come on, you have choosen this letter :P')
            same_letter = True
        self.letters += letter
        if same_letter == False and letter in self.word:
            print('Nice guess')
        else:
            print('Try another letter :P')
        if ' _ ' not in self.grid:
            return 'win'

def main():
    Hangman.file_with_words()
    Hangman.hello()
    words = Hangman.read_words()
    hangman = Hangman(random.choice(words))
    attempts = 0
    while attempts < 10:
        hangman.show_grid()
        result = hangman.ask_letter()
        attempts += 1
        if result == 'win':
            print('Congratz')
            break
    else:
        print('No more tries, unlucky')
    print('The words is ' + hangman.word)

main()
