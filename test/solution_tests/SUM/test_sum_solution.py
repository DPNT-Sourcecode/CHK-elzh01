import pytest

from lib.solutions.SUM.sum_solution import SumSolution


class TestSum:
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(0, 0) == 0
        assert SumSolution().compute(100, 100) == 200
        assert SumSolution().compute(64, 37) == 101

    def test_x_validated_type(self):
        with pytest.raises(TypeError):
            assert SumSolution().compute("1", 2) == 3

    def test_x_validated_lower_bound(self):
        with pytest.raises(ValueError):
            assert SumSolution().compute(-1, 2) == 3

    def test_x_validated_upper_bound(self):
        with pytest.raises(ValueError):
            assert SumSolution().compute(101, 2) == 3

    def test_y_validated_type(self):
        with pytest.raises(TypeError):
            assert SumSolution().compute(1, "2") == 3

    def test_y_validated_lower_bound(self):
        with pytest.raises(ValueError):
            assert SumSolution().compute(1, -1) == 3

    def test_y_validated_upper_bound(self):
        with pytest.raises(ValueError):
            assert SumSolution().compute(1, 101) == 3

