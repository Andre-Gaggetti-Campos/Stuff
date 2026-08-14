import random

wordlist = [
    "apple", "argent", "allow", "apostille",
    "bee", "bean", "berate", "brought",
    "cat", "critical", "candle", "crane",
    "dog", "dance", "direct", "dream",
    "eagle", "early", "enter", "equal",
    "fish", "fable", "forest", "friend",
    "goat", "grape", "green", "great",
    "house", "happy", "honest", "horse",
    "ice", "ideal", "image", "island",
    "jacket", "jelly", "jungle", "judge",
    "kite", "kind", "kitchen", "knock",
    "lion", "lemon", "light", "little",
    "moon", "magic", "market", "music",
    "night", "noble", "notice", "number",
    "orange", "ocean", "often", "order",
    "paper", "peace", "people", "pretty",
    "queen", "quick", "quiet", "quite",
    "rabbit", "radio", "ready", "river",
    "sun", "small", "smart", "strong",
    "table", "teach", "think", "travel",
    "umbrella", "uncle", "under", "unique",
    "van", "value", "visit", "voice",
    "water", "watch", "white", "world",
    "xylophone", "xenon", "xerox", "xylem",
    "yellow", "young", "youth", "yummy",
    "zebra", "zero", "zinc", "zone"]

def game():

    name = input("What is your name?\n")
    print(f"Hello {name}.")

    word = random.choice(wordlist)
    guesses = 0
    max_length = len(word)*2
    guess_word = ['-']*len(word)
    matches = 0

    print("Try and guess my word. You may only guess one letter at a time.")

    while True:

        if guesses >= max_length:
            print(f"You took too long. The word was {word}.")
            break

        while True:

            guess = input()

            if guess.isalpha() and len(guess) == 1:
                guess = guess.lower()
                break
            else:
                print("Please input a letter.")

        good_guess = False
        for i in range (0, len(word)):
            if guess == word[i] and guess_word[i] == '-':
                good_guess = True
                guess_word[i] = guess
                matches += 1
                sum_word = ''.join(guess_word)

        if not good_guess:
            print("Bad guess.")
        else:
            print(f"Nice guess. So far you have {sum_word}")

        guesses += 1

        if matches == len(word):
            print(f"You got the word in {guesses} guesses.")
            break

if __name__ == '__main__':
    game()
