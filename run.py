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
        print(" A B C D E F G H I")
        print(" +-+-+-+-+-+-+-+-+")
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
        for i in range(10):
            self.x_row, self.y_column = random.randint(0, 9), 
            random.randint(0, 9)
            while self.board[self.x_row][self.y_column] == "#":
                self.x_row, self.y_column = random.randint(0, 9), 
                random.randint(0, 9)
            self.board[self.x_row][self.y_column] = "#"
            return self.board


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

            y_column = input("Please enter the column of your guess: ")
            while y_column not in 'ABCDEFGHI':
                print("Not an avilable column, please select again")
                x_row = input("Please enter the column of your guess: ")
            return int(x_row) - 1, get_letter_to_num()[y_column]
        except ValueError and KeyError:
            print("Invalid input")
            return self.get_input()

    def destroy_ships(self):
        