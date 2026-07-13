class CompanyNotFoundError(Exception):
    """Raised when a company cannot be found in Yahoo Finance."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        super().__init__(f"Company '{symbol}' not found.")