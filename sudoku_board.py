from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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
