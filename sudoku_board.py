from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for x in range(1,10): #loop 1-9
            if x % 3 == 1 and x != 1: # start a new block on row 4 and 7
                s += "\n" 
            for y in range(1,10):
                if y % 3 == 1 and y != 1: #add an extra space at column 4 and 7
                    s += " "
                s += str(self.sudoku[(x,y)]) # get the number at coordinates (x,y)
                s += " "
            s += "\n" #Create a newline after filling each row
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        board = {}
        for symbol in model.symbols(shown=True):
            x = symbol.arguments[0].number
            y = symbol.arguments[1].number
            n = symbol.arguments[2].number
            board[(x,y)] = n
        return cls(board)
