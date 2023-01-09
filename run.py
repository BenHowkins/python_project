#Imports
from random import randint


class Board:
    """
    Basics of the game board including creating the board
    """

    def __init__(self, board):
        self.board = board


    def get_letter_to_num():
        """
        Converts the letters of the columns into numbers
        so it can be used in the user input
        """
        letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, 
        "G": 6, "H": 7, "I": 8}
        return letter_to_num


    def print_board(self):
        """
        Print the board to the user to play the game
        """
        print("  A B C D E F G H I")
        print(" +-+-+-+-+-+-+-+-+-+")
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
        for ship in range(10):
            ship_x_row, ship_y_column = randint(0,9), randint(0,9)
        while self.board[ship_x_row][ship_y_column] =='#':
            ship_x_row, ship_y_column = randint(0, 9), randint(0, 9)
        self.board[ship_x_row][ship_y_column] = '#'


    def get_input(self):
        """
        Collects the user input and checks to see if it is valid,
        weither that is an available section or correct data type
        """
        try:
            x_row = input("Please enter the row of your guess: ")
            while x_row not in '123456789':
                print("Not an avilable row, please select again")
                x_row = input("Please enter the row of your guess: ")

            y_column = input("Please enter the column of your guess: ").upper()
            while y_column not in 'ABCDEFGHI':
                print("Not an avilable column, please select again")
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


def run_game():
    """
    Creates all the key elements of the game.
    Including: creating the guess board and computer board containig the ships,
    placing the ships in the computer board, tracking number of turns 
    """
    guess_board = Board([[" "] * 9 for i in range(9)])
    computer_board = Board([[" "] * 9 for i in range(9)])
    Ships.create_ships(computer_board)
    # Start with 50 turns
    turns = 50
    while turns > 0:
        # Print guess board
        Board.print_board(guess_board)
        # Get user's input for guess
        user_x_row, user_y_column = Ships.get_input(object)
        # Check for duplicate guess
        while guess_board.board[user_x_row][user_y_column] == "x" or guess_board.board[user_x_row][user_y_column] == "#":
            print("You've already guessed here. Please pick again")
            user_x_row, user_y_column = Ships.get_input(object)
        # Check if guess was hit or miss
        if computer_board.board[user_x_row][user_y_column] == "#":
            print("BOOM\nDirect Hit, Battleship sunk")
            guess_board.board[user_x_row][user_y_column] = "#"
        else:
            print("SPLASH\nAll you hit was water, Battleships missed")
            guess_board.board[user_x_row][user_y_column] = "x"
        # Check if game has been won, lost or continues
        if Ships.destroyed_ships(guess_board) == 10:
            print("You sunk the entire fleet of 10.\n YOU WIN")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns left")
            if turns == 0:
                print("Sorry the fleet got away.\n YOU LOSE")
                Board.print_board(guess_board)
                break

run_game()