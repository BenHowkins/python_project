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

    def print_board(self):
        """
        Print the board to the user to play the game
        """
        print("  1 2 3 4 5   ")
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
        while True:
            try:
                x_row = int(input("Enter a row number between 1-5 >: "))
                y_column = int(input("Enter a column number between 1-5 >: "))
            except ValueError:
                print("Only enter number!")
                continue
            if x_row not in range(1, 6) or y_column not in range(1, 6):
                print("\nThe numbers must be between 1-5!")
                continue

            return int(x_row) - 1, int(y_column) - 1

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
    explains the game to them.
    """
    print("+--------------------------------+\n"
          "  Welcome To Tactical Sea Combat  \n"
          "+--------------------------------+")
    print("Hello There. For Security Reasons Can We Please Have Your Name?")
    players_name = input("Please Enter Your Name: \n")
    print("+--------------------------------+")
    slow_print(f"ACCESS GRANTED.\nWelcome Admiral {players_name}")
    print("+--------------------------------+")
    slow_print("The Current Situation Is As Follows:")
    print("+--------------------------------+")
    slow_print("A Rouge Submarine Has Been Seen In Our Waters")
    print("+--------------------------------+")
    slow_print("We Have Narrowed It Location To A 5 Mile Square Area\n"
               "And We Need Your Tactical Expertise To Defeat The Enemy\n"
               "However We Only Have 10 Missiles Left At Our Disposal")
    print("+--------------------------------+")
    slow_print("So When You Are Ready Please Make Your Way To The Bridge")
    print("+--------------------------------+")


def start_input():
    """
    A data input which checks if they are ready to play the game
    """
    while True:
        try:
            start_game = input("Please Press Y To Begin: \n").upper()
        except EOFError:
            print("Invalid Input. Please Enter Again")
            continue
        if start_game == "Y":
            break
        else:
            print("Invalid Input. Please Enter Again")


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
            print("You've Already Guessed Here. Please Pick Again")
            user_x_row, user_y_column = Ship.get_input(object)
        # Check if guess was hit or miss
        if computer_board.board[user_x_row][user_y_column] == "#":
            guess_board.board[user_x_row][user_y_column] = "#"
        else:
            print("SPLASH")
            slow_print("All You Hit Was Water, Submarine Missed")
            guess_board.board[user_x_row][user_y_column] = "x"
        # Check if game has been won, lost or continues
        if Ship.destroyed_ship(guess_board) == 1:
            print("BOOM")
            slow_print("You Sunk The Rouge Submarine.\nYOU WIN")
            Board.print_board(guess_board)
            break
        else:
            turns -= 1
            print(f"We Have {turns} Missiles Left Admiral.")
            if turns == 0:
                slow_print("Sorry Admiral The Enemy Has Escaped.\nYOU LOSE")
                Board.print_board(computer_board)
                print("The Enemy's location Was Here")


def play_again():
    """
    Creates a function to see if they want to play again
    and if they do restart the game
    """
    while True:
        try:
            restart = input('Play Again Admiral: (Y)es/ (N)o?\n').upper()
        except EOFError:
            print("Invalid Input. PLease Try Again")
            continue
        if restart == 'N':
            slow_print("Thank You For Your Service Admiral")
            break
        elif restart == 'Y':
            run_game()
        else:
            print('Play Again Admiral: (Y)es/ (N)o?\n')


def play_game():
    """
    A function which calls the intro and run_game functions
    so the player can play the game
    """
    intro()
    start_input()
    run_game()
    play_again()


play_game()
