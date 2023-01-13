"""
Imported files from python library
"""
from random import randint
from time import sleep


class Board:
    """
    Creates the basics of the game board, converts letter guesses into
    numbers and prints the board
    """

    def __init__(self, board):
        self.board = board

    def get_letter_to_num(self):
        """
        Converts the letters of the columns into numbers
        so it can be used in the user input
        """
        letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letter_to_num

    def print_board(self):
        """
        Print the board to the user to play the game
        """
        print("  A B C D E   ")
        print(" +-+-+-+-+-+ ")
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1


class Ship:
    """
    Deals with the main functions of the ship including
    creating and placing the ship, getting user input
    and checking if they've been destroyed
    """
    def __init__(self, board):
        self.board = board

    def create_ship(self):
        """
        Creates and places the ship on the guess board
        """
        ship_x_row = randint(0, 4)
        ship_y_column = randint(0, 4)
        self.board[ship_x_row][ship_y_column] = '#'
        return self.board

    def get_input(self):
        """
        Collects the user input and checks to see if it is valid,
        if that is an available selection and correct data type
        """
        try:
            x_row = input("Please enter your row guess: \n")
            while x_row not in '12345':
                print("Not an available row, please select again")
                x_row = input("Please enter your row guess: \n")

            y_column = input("Please enter your column guess: \n").upper()
            while y_column not in 'ABCDE':
                print("Not an available column, please select again")
                y_column = input("Please enter your column guess: \n").upper()
            return int(x_row) - 1, Board.get_letter_to_num(self)[y_column]
        except (ValueError, KeyError):
            print("Invalid input")
            return self.get_input()

    def destroyed_ship(self):
        """
        Checks to see if the ship has been destroyed
        """
        ship_destroyed = 0
        for row in self.board:
            for column in row:
                if column == "#":
                    ship_destroyed += 1
        return ship_destroyed


def slow_print(txt):
    """
    Function which allows the text to print out at a slower rate
    used to give the appearance of it being typed out
    """
    for letter in txt:
        print(letter, end='', flush=True)
        sleep(0.15)
    print()


def intro():
    """
    An introduction into the game, which gets the player's name,
    explains the game to them and checks if they are ready to play
    """
    print("+--------------------------------+\n"
          "  Welcome To Tactical Sea Combat  \n"
          "+--------------------------------+")
    print("Hello There. For security reasons can we please have your name?")
    players_name = input("Please enter your name: \n")
    print("+--------------------------------+")
    slow_print(f"ACCESS GRANTED.\nWelcome Admiral {players_name}")
    print("+--------------------------------+")
    slow_print("The current situation is as follows:")
    print("+--------------------------------+")
    slow_print("A Rouge Submarine has been seen in our waters")
    print("+--------------------------------+")
    slow_print("We have narrowed it location to a 5 mile square area\n"
               "And we need your tactical expertise to defeat the enemy\n"
               "However we only have 10 missiles left at our disposal")
    print("+--------------------------------+")
    slow_print("So when you are ready please make your way to the bridge")
    print("+--------------------------------+")

    start_game = input("Please press Y to to begin the game: \n").upper()
    if start_game != "Y":
        start_game = input("Please press Y to to begin the game: \n").upper()


def run_game():
    """
    Creates all the key elements of the game.
    Including: creating the guess board and computer board containing
    the ships, placing the ships in the computer board, tracking turns
    """
    guess_board = Board([[" "] * 5 for i in range(5)])
    computer_board = Board([[" "] * 5 for i in range(5)])
    Ship.create_ship(computer_board)
    # Start with 10 turns
    turns = 10
    while turns > 0:
        # Print guess board
        Board.print_board(guess_board)
        # Get user's input for guess
        user_x_row, user_y_column = Ship.get_input(object)
        # Check for duplicate guess
        while guess_board.board[user_x_row][user_y_column] == "x":
            print("You've already guessed here. Please pick again")
            user_x_row, user_y_column = Ship.get_input(object)
        # Check if guess was hit or miss
        if computer_board.board[user_x_row][user_y_column] == "#":
            guess_board.board[user_x_row][user_y_column] = "#"
        else:
            print("SPLASH")
            slow_print("All you hit was water, Submarine missed")
            guess_board.board[user_x_row][user_y_column] = "x"
        # Check if game has been won, lost or continues
        if Ship.destroyed_ship(guess_board) == 1:
            print("BOOM")
            slow_print("You sunk the rouge submarine.\nYOU WIN")
            Board.print_board(guess_board)
            break
        else:
            turns -= 1
            print(f"We have {turns} missiles left Admiral.")
            if turns == 0:
                slow_print("Sorry Admiral the enemy got away.\nYOU LOSE")
                Board.print_board(computer_board)
                print("The enemy was here")


def play_again():
    """
    Creates a function to see if they want to play again
    and if they do restart the game
    """
    while True:
        restart = input('Do You Wish To Play Again: (Y)es/ (N)o?\n').upper()
        if restart == 'N':
            slow_print("Thank You For Your Service Admiral")
            break
        elif restart == 'Y':
            run_game()
        else:
            restart = input('do you want to restart: (Y)es/ (N)o?\n').upper()


def play_game():
    """
    A function which calls the intro and run_game functions
    so the player can play the game
    """
    intro()
    run_game()
    play_again()


play_game()
