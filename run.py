#Imports
from random import randint


class Gameboard:
    """
    Basics of the game board including creating the board and the ships
    as well as player inputs
    """
    def __init__(self, board):
        self.board = board
    
    def get_letter_to_num():
        """
        Converts the letters of the columns into numbers
        so it can be used in the user input
        """
        letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        return letter_to_num
    
    def print_board(self):
        """
        Print the board to the user to play the game
        """
        print(" A B C D E F G H I J")
        print(" +-+-+-+-+-+-+-+-+-+")
        row_num = 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num += 1
        
    def create_ships(self):
        """
        Creates and places the ships on the guess board
        whilst also checking there isn't already a ship there
        """
        for i in range(10):
            self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            while self.board[self.x_row][self.y_column] == "#":
                self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            self.board[self.x_row][self.y_column] = "#"
            return self.board