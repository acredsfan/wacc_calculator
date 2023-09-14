class WACC:
    def __init__(self, equity: float, debt: float, equity_cost: float, debt_cost: float, tax_rate: float):
        self.equity = equity
        self.debt = debt
        self.equity_cost = equity_cost
        self.debt_cost = debt_cost
        self.tax_rate = tax_rate

    def calculate(self) -> float:
        """
        Calculates and returns the Weighted Average Cost of Capital (WACC) using the formula:
        WACC = (E/V) * Re + (D/V) * Rd * (1 - Tc)
        where:
        E = Market value of equity
        D = Market value of debt
        V = Total market value of equity and debt (E + D)
        Re = Cost of equity
        Rd = Cost of debt
        Tc = Corporate tax rate
        """
        try:
            v = self.equity + self.debt
            if v == 0:
                raise ZeroDivisionError("Total market value of equity and debt (E + D) cannot be zero.")
            wacc = (self.equity / v) * self.equity_cost + (self.debt / v) * self.debt_cost * (1 - self.tax_rate)
            return wacc
        except ZeroDivisionError as zde:
            print(zde)
            return None
        except Exception as e:
            print(f"Error occurred while calculating WACC: {e}")
            return None
