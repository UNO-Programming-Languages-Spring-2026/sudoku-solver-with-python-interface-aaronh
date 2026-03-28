import sys, clingo
from sudoku_board import Sudoku

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        if files:
            with open(files[0]) as file:
                board = Sudoku.from_str(file.read())
        if not files:
            board = Sudoku.from_str(sys.stdin.read())
        ctl.load("sudoku2.lp")
        ctl.load("sudoku_py.lp")
        context = Context(board)
        ctl.ground([("base", [])], context=context)
        ctl.solve()
    
    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)
        sys.stdout.flush()

class Context:
    def __init__(self, board: Sudoku):
        self.board = board
    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        for (x,y), n in self.board.sudoku.items():
            symbols.append(clingo.Tuple_([clingo.Number(x), clingo.Number(y), clingo.Number(n)])) #add each initial rule to the list
        return symbols
clingo.application.clingo_main(ClingoApp())