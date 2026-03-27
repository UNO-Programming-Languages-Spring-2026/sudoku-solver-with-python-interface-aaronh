import sys, clingo

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for file in files:
            ctl.load(file)
        if not files:
            ctl.load("-")
        ctl.load("sudoku2.lp")
        ctl.ground([("base", [])])
        ctl.solve()
    
    def print_model(self, model, printer):
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
        sys.stdout.flush()
clingo.application.clingo_main(ClingoApp()) 
    