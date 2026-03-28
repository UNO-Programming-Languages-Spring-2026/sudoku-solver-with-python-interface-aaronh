import sys, clingo
from sudoku_board import Sudoku

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for file in files:
            ctl.load(file)
        if not files:
            ctl.load("-")
        ctl.load("sudoku2.lp")
        ctl.ground([("base", [])])
        ctl.solve()
    
    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)
        sys.stdout.flush()
    
clingo.application.clingo_main(ClingoApp())