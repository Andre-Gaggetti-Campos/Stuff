import random

def game():
    print("Welcome to the game!\n If you want to play, type 'yes', else type 'no'.")

    while True:

        cont = input()

        if cont=='yes' or cont=='no':
            break

        print("Please type 'yes' or 'no'.")

    if cont=='no':
        return

    randomNumber = random.randint(1, 100)

    print("Try to guess my number (1-100) :)")

    while True:

        while True:

            number = input()

            try:
                intNumber = int(number)
            except ValueError:
                print("Please say an integer.")
            else:
                break

        if intNumber < randomNumber:
            print("Too Low.")
        elif intNumber > randomNumber:
            print("Too High.")
        else:
            print("You got it :D")
            break

if __name__ == '__main__':
    game()
