class InvalidFilePathError(Exception):
    """
    Exception raised when the provided file path is invalid.
    """
    def __init__(self, file_path, message="Invalid file path provided."):
        self.file_path = file_path
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_path} -> {self.message}'


class ParsingError(Exception):
    """
    Exception raised when an error occurs during parsing of the 10K filing.
    """
    def __init__(self, message="Error occurred during parsing."):
        self.message = message
        super().__init__(self.message)


class WACCCalculationError(Exception):
    """
    Exception raised when an error occurs during the calculation of WACC.
    """
    def __init__(self, message="Error occurred during WACC calculation."):
        self.message = message
        super().__init__(self.message)
