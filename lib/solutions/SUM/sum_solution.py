class SumSolution:
    def compute(self, x: int, y: int) -> int:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("x and y must be integers.")
        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise ValueError("x and y must be between 0 and 100 inclusive.")
        return x + y
