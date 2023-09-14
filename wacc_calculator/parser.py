## parser.py

from bs4 import BeautifulSoup

class Parser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> (float, float, float, float, float):
        """
        Parses the 10K filing and returns the necessary data for WACC calculation.
        The returned tuple contains the following values in order:
        - equity
        - debt
        - equity cost
        - debt cost
        - tax rate
        """
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()

            soup = BeautifulSoup(data, 'html.parser')

            # The following lines are placeholders. 
            # The actual implementation depends on the structure of the 10K filing.
            equity = float(soup.find('equity').text)
            debt = float(soup.find('debt').text)
            equity_cost = float(soup.find('equity_cost').text)
            debt_cost = float(soup.find('debt_cost').text)
            tax_rate = float(soup.find('tax_rate').text)

            return equity, debt, equity_cost, debt_cost, tax_rate
        except Exception as e:
            print(f"Error occurred while parsing the file: {e}")
            return None
