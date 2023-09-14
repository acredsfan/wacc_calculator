## main.py
import argparse
import cProfile
from parser import Parser
from wacc import WACC
from exceptions import InvalidFilePathError, ParsingError, WACCCalculationError

class Main:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def run(self) -> None:
        """
        Runs the program.
        """
        try:
            parser = Parser(self.file_path)
            equity, debt, equity_cost, debt_cost, tax_rate = parser.parse()

            if equity is None or debt is None or equity_cost is None or debt_cost is None or tax_rate is None:
                raise ParsingError()

            wacc_calculator = WACC(equity, debt, equity_cost, debt_cost, tax_rate)
            wacc = wacc_calculator.calculate()

            if wacc is None:
                raise WACCCalculationError()

            print(f"The calculated WACC is: {wacc}")
        except InvalidFilePathError as ifpe:
            print(ifpe)
        except ParsingError as pe:
            print(pe)
        except WACCCalculationError as wce:
            print(wce)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate WACC from a 10K filing.')
    parser.add_argument('file_path', type=str, help='The path to the 10K filing.')
    args = parser.parse_args()

    main = Main(args.file_path)

    # Use cProfile to identify bottlenecks and optimize the program for efficiency.
    profiler = cProfile.Profile()
    profiler.enable()
    main.run()
    profiler.disable()
    profiler.print_stats()
