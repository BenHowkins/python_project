#Imports
from random import randint


class Board:
    """
    Creates the basics of the game board, converts letter guesses into
    numbers and prints the board
    """

    def __init__(self, board):
        self.board = board


    def get_letter_to_num():
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

class Ships:
    """
    Deals with the main functions of the ships including
    creating and placing the ships, getting user input
    and checking if they've been destroyed
    """
    def create_ships(self):
        """
        Creates and places the ships on the guess board
        whilst also checking there isn't already a ship there
        """
        for ship in range(1):
            ship_x_row, ship_y_column = randint(0,4), randint(0,4)
        self.board[ship_x_row][ship_y_column] = '#'
        return self.board


    def get_input(self):
        """
        Collects the user input and checks to see if it is valid,
        if that is an available selection and correct data type
        """
        try:
            x_row = input("Please enter the row of your guess: ")
            while x_row not in '12345':
                print("Not an available row, please select again")
                x_row = input("Please enter the row of your guess: ")

            y_column = input("Please enter the column of your guess: ").upper()
            while y_column not in 'ABCDE':
                print("Not an available column, please select again")
                y_column = input("Please enter the column of your guess: ").upper()
            return int(x_row) - 1, Board.get_letter_to_num()[y_column]
        except ValueError and KeyError:
            print("Invalid input")
            return self.get_input()


    def destroyed_ships(self):
        """
        Checks to see if a ship has been destroyed
        and keeps count on how many are left on the board
        and how many have been destroyed
        """
        ships_destroyed = 0
        for row in self.board:
            for column in row:
                if column == "#":
                    ships_destroyed += 1
        return ships_destroyed


def intro():
    """
    An introduction into the game, which gets the player's name,
    explains the game to them and checks if they are ready to play
    """
    print("+--------------------------------+\n"
          "  Welcome To Tactical Sea Combat  \n"
          "+--------------------------------+")
    print("Hello There. For security reasons can we please have your name?")
    players_name = input("Please enter your name: ")
    print("+--------------------------------+")
    print(f"Access granted. Welcome to the war room Admiral {players_name}")
    print("+--------------------------------+")
    print("The current situation is as follows: \n"
          "+--------------------------------+\n"
          "A fleet of 10 enemy Battleships has been seen in our waters\n"
          "+--------------------------------+\n"
          "And we need your tactical expertise to defeat the enemy\n"
          "Using only the 50 missiles we have left at our disposals\n"
          "+--------------------------------+\n"
          "So when you are ready please make your way to the bridge\n"
          "+--------------------------------+")
    
    start_game = input("Please press Y to to begin the game: ").upper()
    if start_game != "Y":
        start_game = input("Please press Y to to begin the game: ").upper()


def run_game():
    """
    Creates all the key elements of the game.
    Including: creating the guess board and computer board containing the ships,
    placing the ships in the computer board, tracking number of turns 
    """
    guess_board = Board([[" "] * 5 for i in range(5)])
    computer_board = Board([[" "] * 5 for i in range(5)])
    Ships.create_ships(computer_board)
    # Start with 10 turns
    turns = 10
    while turns > 0:
        # Print guess board
        Board.print_board(guess_board)
        # Get user's input for guess
        user_x_row, user_y_column = Ships.get_input(object)
        # Check for duplicate guess
        while guess_board.board[user_x_row][user_y_column] == "x":
            print("You've already guessed here. Please pick again")
            user_x_row, user_y_column = Ships.get_input(object)
        # Check if guess was hit or miss
        if computer_board.board[user_x_row][user_y_column] == "#":
            guess_board.board[user_x_row][user_y_column] = "#"
        else:
            print("SPLASH\nAll you hit was water, Battleships missed")
            guess_board.board[user_x_row][user_y_column] = "x"
        # Check if game has been won, lost or continues
        if Ships.destroyed_ships(guess_board) == 1:
            print("BOOM\nYou sunk the rouge submarine.\nYOU WIN")
            Board.print_board(guess_board)
            break
        else:
            turns -= 1
            print(f"We have {turns} missiles left")
            if turns == 0:
                print("Sorry the fleet got away.\n YOU LOSE")
                Board.print_board(computer_board)
                print("The enemy was here")
                break

def play_game():
    """
    A function which calls the intro and run_game functions
    so the player can play the game
    """
    intro()
    run_game()


play_game()